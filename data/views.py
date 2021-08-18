from django.shortcuts import render, redirect
import csv

# import from this project
from .forms import *
from .models import *

def home(request):
    addForm = NewDataForm()
    removeForm = RemoveDataForm()
    error_message = None

    if request.POST:

        # === add new data ===

        if 'add' in request.POST:
            form = NewDataForm(request.POST)
            if form.is_valid:
                # save data to Tempaerature model
                form.save()

                return redirect('home')

        #  === remove data ===

        if 'remove' in request.POST:
            form = RemoveDataForm(request.POST)
            if form.is_valid:
                # remove data to Tempaerature model
                x_value = form.cleaned_data["x_value"]
                y_value = form.cleaned_data["y_value"]

                try:
                    obj = Temperature.objects.get(x=x_value, y=y_value)
                    obj.remove()
                    return redirect('home')
                
                except:
                    error_message = 'No such data...'
                

    return render(request, 'home.html', {
        'addForm': addForm,
        'removeForm': removeForm,
        'error_message': error_message,
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
