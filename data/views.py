from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import csv

# import from this project
from .forms import *
from .models import *

def home(request):

    # === graphs ===

    files = Csv.objects.filter(activated=True)

    ''' MISUNDERSTANDING
    addForm = NewDataForm()
    removeForm = RemoveDataForm()
    error_message = None

    if request.POST:

        # === add new data ===

        if 'add' in request.POST:
            form = NewDataForm(request.POST)
            if form.is_valid():
                # save data to Tempaerature model
                form.save()

                return redirect('home')

        #  === remove data ===

        if 'remove' in request.POST:
            form = RemoveDataForm(request.POST)
            if form.is_valid():
                # remove data to Tempaerature model
                x_value = form.cleaned_data["x_value"]
                y_value = form.cleaned_data["y_value"]

                try:
                    obj = Temperature.objects.get(x=x_value, y=y_value)
                    obj.delete()
                    return redirect('home')
                
                except:
                    error_message = 'No such data...'
        '''      

    return render(request, 'home.html', {
        'files': files,
        # 'addForm': addForm,
        # 'removeForm': removeForm,
        # 'error_message': error_message,
    })

def graph(request, id):

    file = Csv.objects.get(id=id)

    output = []

    with open(file.file.path, 'r') as f:
            reader = csv.reader(f)
            data = [row for row in reader]

    # set up the graph
    for i in range(1, len(data)):
        output.append("{ x: " + str(float(data[i][0])*40) +
        ", y: " + str(float(data[i][1])*40) + ", value: " +
        str(data[i][2]) + "},")

    files = Csv.objects.filter(activated=True)
    
    if request.POST:
        file.delete()
        return redirect('home')

    return render(request, 'graph.html', {
        'file': file,
        'files': files,
        'data' : output,
    })

def upload_file(request):
    success_message = None
    form = CsvForm()

    if request.POST:
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():

            # save file to Csv model

            form.save()
            form = CsvForm()

            # save data to Temperature model
            
            obj = Csv.objects.get(activated=False)

            '''MISUNDERSTANDING
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
            '''
            
            obj.activated = True
            obj.save()
            success_message = 'Uploaded successfully.'

    return render(request, 'upload.html', {
        'success_message': success_message,
        'form': form,
    })
