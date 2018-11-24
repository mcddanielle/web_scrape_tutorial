Used the following weblink.
https://www.dataquest.io/blog/web-scraping-tutorial-python/

Goals for skill: help Ryan Carle scrape data from his driveline acct.

issues with tutorial: the temperature data was not structured as written in the tutorial.  I wrote a few work arounds.  There is no place to write comments on the webpage, and there is not an obvious way to email the developer.

I had to modify the code to get the temperature for right now by including:

  #NOW
  current = soup.find(id='current_conditions-summary')
  current_items = current.find_all("p")
  temp = current_items[1].get_text()
  print(temp)

Then later in the code, I couldn't easily include temperature in the pandas data table because it had fewer rows in the data set than the other elements.