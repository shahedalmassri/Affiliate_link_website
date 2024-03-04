from flask import Flask, redirect, request, session, render_template, abort
import sqlite3

#Note: for running flask use this guide https://code.visualstudio.com/docs/python/tutorial-flask
app = Flask(__name__)
app.secret_key = "P0T8S3_MN61RQ9&2DYW"

#Replace with allowable IP addresses
allowed_ips = ["203.156.78.224"]

#This is the admin-only page route
@app.route('/admin', methods=["GET", "POST"])
def admin_dashboard():
    #Only allowed IPs are permitted to access this page
    #get client's IP from the request
    client_ip = request.remote_addr 

    #return a 403 Forbidden request if the IP is not allowed
    if client_ip not in allowed_ips:
        abort(403)   

    if request.method == "POST":
        action = request.form.get('action')
        
        #Adding a new card
        if action == "add":
            image_link = request.form['image_link']
            title = request.form['title']
            product_link = request.form['product_link']
            subtitle = request.form['subtitle']
            body_text = request.form['body_text']

            #connect SQL database to db variable
            conn = sqlite3.connect('website.db')
            db = conn.cursor()

            # Execute SQL insertion query
            db.execute("INSERT INTO cards(image_link,title,product_link, subtitle,body_text) VALUES (?, ?, ?, ? ,?)", (image_link, title, product_link, subtitle, body_text))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            return redirect('/admin')
        
        #Editing a card
        elif action == "edit":
            #connect SQL database to db variable
            conn = sqlite3.connect('website.db')
            db = conn.cursor()

            #Retrieve the old values from the database (This is so if a value isn't given, it doesn't overwrite an old one)
            card_id = request.form['card_id']
            db.execute("SELECT image_link, title, product_link, subtitle, body_text FROM cards WHERE card_id=?", (card_id,))
            old_values = db.fetchone()
            old_values_dict = {
                'image_link': old_values[0],
                'title': old_values[1],
                'product_link': old_values[2],
                'subtitle': old_values[3],
                'body_text': old_values[4]
            }

            #Get the new values from the form
            image_link = request.form['image_link']
            title = request.form['title']
            product_link = request.form['product_link']
            subtitle = request.form['subtitle']
            body_text = request.form['body_text']

            #Check if fields are empty and use old values if they are
            if not image_link:
                image_link = old_values_dict['image_link']
            if not title:
                title = old_values_dict['title']
            if not product_link:
                product_link = old_values_dict['product_link']
            if not subtitle:
                subtitle = old_values_dict['subtitle']
            if not body_text:
                body_text = old_values_dict['body_text']

            # Execute an update SQL query
            db.execute("UPDATE cards SET image_link=?, title=?, product_link=?, subtitle=?, body_text=? WHERE card_id=?",(image_link, title, product_link, subtitle, body_text, card_id))

             # Commit the changes and close the connection
            conn.commit()
            conn.close()
            return redirect('/admin')
    
        #Deleting a card
        elif action == "delete":
            #connect SQL database to db variable
            conn = sqlite3.connect('website.db')
            db = conn.cursor()

            card_id = request.form['card_id']
            #Execute a SQL Delete query
            db.execute("DELETE FROM cards WHERE card_id=?", (card_id,))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            return redirect('/admin')
        
        return render_template('admin.html')
    
    #GET route  
    else:
        #connect SQL database to db variable
        conn = sqlite3.connect('website.db')
        db = conn.cursor()

        # Execute SQL query
        db.execute("SELECT * FROM cards")
        
        #Fetch column names from cursor description
        column_names = [desc[0] for desc in db.description]

        #Fetch the results into a list of dictionaries
        cards = [dict(zip(column_names, row)) for row in db.fetchall()]
        #newest first
        cards.reverse()

        return render_template("admin.html", cards=cards)

#This is the public page route
@app.route('/')
def public_page():
    #connect SQL database to db variable
    conn = sqlite3.connect('website.db')
    db = conn.cursor()

    # Execute SQL query
    db.execute("SELECT * FROM cards")
    
    #Fetch column names from cursor description
    column_names = [desc[0] for desc in db.description]

    #Fetch the results into a list of dictionaries
    cards = [dict(zip(column_names, row)) for row in db.fetchall()]

    #Reverse order, show newest to oldest 
    cards.reverse()
    return render_template("public.html", cards=cards)