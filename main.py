from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def grade_calculator():
  grade = ""
  RP = ""
  if request.method == 'POST':
        # Get the input values from the form
        type = request.form.get('type')
        engagement_score = int(request.form['engagement_score'])
        mid_year_score = float(request.form['mid_year_score'])
        promo_score = float(request.form['promo_score'])
        
        # Validate the input values
        if engagement_score < 0 or engagement_score > 10:
            return render_template('index.html', error='Engagement score must be between 0 and 10.')
        if mid_year_score < 0 or mid_year_score > 100:
            return render_template('index.html', error='Mid-year examination score must be between 0 and 100.')
        if promo_score < 0 or promo_score > 100:
            return render_template('index.html', error='Promo exam score must be between 0 and 100.')

        # Calculate the overall grade
        total_score = engagement_score * 0.1 + mid_year_score * 0.15 + promo_score * 0.75
      
        if type == 'H1':
          if total_score >= 70:
            grade = 'A'
            RP = '20'
          elif total_score == 69:
            grade = 'Nice (B)'
            RP = '17.5'
          elif total_score >= 60:
            grade = 'B'
            RP = '17.5'
          elif total_score >= 55:
            grade = 'C'
            RP = '15'
          elif total_score >= 50:
            grade = 'D'
            RP = '12.5'
          elif total_score >= 45:
            grade = 'E'
            RP = '10'
          elif total_score >= 40:
            grade = 'S'
            RP = '5'
          else:
            grade = 'U'
            RP = '0'
        else:
          if total_score >= 70:
            grade = 'A'
            RP = '12'
          elif total_score >= 60:
            grade = 'B'
            RP = '8.75'
          elif total_score >= 55:
            grade = 'C'
            RP = '7.5'
          elif total_score >= 50:
            grade = 'D'
            RP = '6.25'
          elif total_score >= 45:
            grade = 'E'
            RP = '5'
          elif total_score >= 40:
            grade = 'S'
            RP = '2.25'
          else:
            grade = 'U'
            RP = '0'


        # Render the result template with the grade
        return render_template('index.html', grade=grade, RP=RP)

  return render_template('index.html', grade=grade, RP=RP)
    # If we get here, it means the request method is GET, so we just render the index page


app.run(host='0.0.0.0', port=81)

