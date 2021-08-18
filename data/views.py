from django.shortcuts import render
import csv

# import from this project
from .forms import *
from .models import *

def home(request):
    addForm = NewDataForm()

    if request.POST:

        # === add new data ===

        form = NewDataForm(request.POST)
        if form.is_valid:

            # save file to Tempaerature model
            form.save()
            form = NewDataForm()

        #  === remove data ===



    return render(request, 'home.html', {
        'addForm': addForm,
    })

def upload_file(request):
    success_message = None
    form = CsvForm()

    if request.POST:
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid:

            # save file to Csv model

            form.save()
            form = CsvForm()

            # save data to Temperature model
            
            obj = Csv.objects.get(activated=False)
            with open(obj.file.path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == "x":
                        pass
                    else:
                        Temperature.objects.create(
                            x = float(row[0]),
                            y = float(row[1]),
                            temperature = float(row[2])
                        )

            obj.activated = True
            obj.save()
            success_message = 'Uploaded successfully.'

    return render(request, 'upload.html', {
        'success_message': success_message,
        'form': form,
    })
