## Install and Run the software

Apart from Python3, you need to install all libraries in requirements.txt via "pip install -r requirements.txt" . To run the server, open this folder and run "py manage.py runserver" in the terminal.

## Technical Description

Users can upload and remove their csv files. Data from each file will be displayed as a heatmap graph -- the hotter temperature, the color becomes more orange/red; the cooler temperature, the color becomes more green/blue. Those data will also save separately for users to manipulate.

## Work Description

I read the instruction first and then make a draft of some pages including what functions.

There was a misunderstanding at the beginning that I thought every data row need to be saved to database for a big scale graph and users will add or remove each data row. That is how the separate add/remove functions came from. But then I think each graph for each file should make more sense that "switching them easily visualise the
condition of the silos at a glance". So I make changes.

In the process, I was not sure which graph should be displayed. Then I do some research and I found a heatmap library which I believe it is suitable for displaying temperature so I learnt and use it.