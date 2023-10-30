from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        height = request.POST.get('height')

        height = int(height)
        weight = int(weight)

        bmi = weight / (height * height)

        if bmi > 34:
            status = "Obese"
        elif bmi > 29:
            status = "Over weight"
        elif bmi > 18:
            status = "Normal Weight"
        else:
            status = "Under Weight"

        results = {"name": name, "bmi": bmi, "status": status}
        return render(request, 'index.html', results)

    # bmi = weight divided height in mtrs squared
    # bmi = weight /(h*h)
    # Use scale: 0 - 18 = Underweight
    #            18.1 - 29 = Normal weight
    #            29.1 - 34 = Overweight
    #            34.1 and above = Obese

    return render(request, 'index.html')
