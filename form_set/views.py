from django.shortcuts import render,redirect
from .models import*
from .forms import*
# Create your views here.

# def home(request):
#     return render(request,'home.html')

def home(request, pk):
    customer=Customer.objects.get(id=pk)
    if request.method == 'GET':
         customerform = invoiceForm(request.GET or None,instance=customer)
         formset = orderFormset()
    # if request.method == 'POST':
    #     customerform = invoiceForm(request.POST)
    #     formset = orderFormset(request.POST)
        # if  formset.is_valid() :
            # first save this book, as its reference will be used in `Author`
            # customer = customerform.save()


    context={'formset': formset,'customerform':customerform}
    return render(request,'home.html',context )

    # if request.method == 'GET':
    #     form = CustomerForm(request.GET or None)
    #     formset_instances = bookFormset(queryset=Book.objects.none())
    # if request.POST:
    #     form=CustomerForm(request.POST)
    #     formset_instances=bookFormset(request.POST)
    #     if form.is_valid():
    #         customer=Customer()
    #         customer.name=form.cleaned_data['name']
    #         customer.save()
    #
    #     if formset_instances.is_valid():
    #
    #         for data in formset_instances:
    #             book=Book()
    #             book.bookname=data.cleaned_data.get('bookname')
    #             book.save()
    #             customer.book.add(book)
    #         customer.save()
    #         return redirect('/')
    # else:
    #     form=CustomerForm()
    #     formset=bookFormset()
    #     context={'form':form,'formset':formset}
    #     return render(request, 'home.html',context)
