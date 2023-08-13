else:
            # Handle the case when the form is not valid
            # For example, you can re-render the same page with the invalid form
            return render(request, 'encyclopedia/create_entry.html',{
                'form': form
                })