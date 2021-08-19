## Install and Run the software

Apart from Python3, you need to install all libraries in requirements.txt via "pip install -r requirements.txt" . To run the server, open this folder and run "py manage.py runserver" in the terminal.

## Technical Description

Users can upload and remove their csv files. By clicking on the file's timestamp link, users will go to that file page. Data from each file will be displayed as a heatmap graph -- the hotter temperature, the color becomes more orange/red; the cooler temperature, the color becomes more green/blue.

![home](https://user-images.githubusercontent.com/68764665/129975703-9ccc9991-9520-4500-b594-652f2c0f89eb.png)
![upload](https://user-images.githubusercontent.com/68764665/129976202-96f96693-daf4-45b7-9c8c-25a10c9763aa.png)
![graph](https://user-images.githubusercontent.com/68764665/129976272-1decaade-6dcd-43ac-b7c9-ff20d302f151.png)

## Work Description

I read the instruction first and then make a draft of some pages including what functions.

There was a misunderstanding at the beginning that I thought every data row need to be saved to database for a big scale graph and users will add or remove each data row. That is how the separate add/remove functions came from. But then I think each graph for each file should make more sense that "switching them easily visualise the
condition of the silos at a glance". So I make changes.

In the process, I was not sure which graph should be displayed. Then I do some research and I found a heatmap library which I believe it is suitable for displaying temperature so I learnt and use it.
