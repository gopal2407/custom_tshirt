import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django import views
from .models import ItemSize, Color, Category, Font, SubCategory, Coupon, Item, Address


class LoginView(views.View):

    def get(self, request):
        # if request.user.is_authenticated:
        template_name = 'custome_app/login.html'
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('admin_view_url')
            elif hasattr(user, 'owner'):
                return redirect('owner_view_url')
            elif hasattr(user, 'customer'):
                return redirect('customer_view_url')
        return render(request, template_name='custome_app/login.html', context={'msg': 'unauthenticated user'})


class AdminView(views.View):
    def get(self, request):
        template_name = 'custome_app/admin_hompage.html'
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        pass


class CustomerView(views.View):

    def get(self, request):
        template_name = 'custome_app/customer_homepage.html'
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        pass


class OwnerView(views.View):

    def get(self, request):
        template_name = 'custome_app/owner_homepage.html'
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        pass


class LogoutView(views.View):

    def get(self, request):
        logout(request)
        return redirect('login_view_url')


# Admin Functionality
class SizeView(views.View):

    def get(self, request, pk=None):
        context = {}

        template_name = 'admin_function/size.html'
        sizes = ItemSize.objects.all()
        context['sizes'] = sizes

        if pk:
            size = sizes.filter(id=pk)

            if str(request.path).endswith('/delete/'):
                context['del_size'] = size[0] if size.exists() else None
            else:
                context['size'] = size[0] if size.exists() else None

        return render(request, template_name, context)

    def post(self, request, pk=None):
        template_name = 'admin_function/size.html'
        try:
            name = request.POST.get('name')
            context = {}
            if pk:

                try:
                    size = ItemSize.objects.get(pk=pk)
                    if str(request.path).endswith('/delete/'):
                        size.delete()
                    else:
                        size.name = name
                        size.save()
                except Exception as e1:
                    return render(request, template_name, context={'error': str(e1)})
            else:
                ItemSize.objects.create(name=name)

            return redirect('size_view_url')
        except Exception as e:
            return render(request, template_name, context={'error': str(e)})


class ColorView(views.View):
    def get(self, request, pk=None):
        context = {}

        template_name = 'admin_function/color.html'
        colors = Color.objects.all()
        context['colors'] = colors

        if pk:
            color = colors.filter(id=pk)

            if str(request.path).endswith('/delete/'):
                context['del_color'] = color[0] if color.exists() else None
            else:
                context['color'] = color[0] if color.exists() else None

        return render(request, template_name, context)

    def post(self, request, pk=None):
        template_name = 'admin_function/color.html'
        try:
            name = request.POST.get('name')
            context = {}
            if pk:

                try:
                    color = Color.objects.get(pk=pk)
                    print(color)
                    if str(request.path).endswith('/delete/'):
                        color.delete()
                    else:
                        color.name = name
                        color.save()
                except Exception as e1:
                    return render(request, template_name, context={'error': str(e1)})
            else:
                Color.objects.create(name=name)

            return redirect('color_view_url')
        except Exception as e:
            return render(request, template_name, context={'error': str(e)})


class CategoryView(views.View):
    def get(self, request, pk=None):
        context = {}

        template_name = 'admin_function/category.html'
        categories = Category.objects.all()
        context['categories'] = categories

        if pk:
            category = categories.filter(id=pk)
            print(category)

            if str(request.path).endswith('/delete/'):
                context['del_category'] = category[0] if category.exists() else None
            else:
                context['category'] = category[0] if category.exists() else None

        return render(request, template_name, context)

    def post(self, request, pk=None):
        template_name = 'admin_function/category.html'
        try:
            name = request.POST.get('name')
            context = {}
            if pk:

                try:
                    category = Category.objects.get(pk=pk)
                    if str(request.path).endswith('/delete/'):
                        category.delete()
                    else:
                        category.name = name
                        category.save()
                except Exception as e1:
                    return render(request, template_name, context={'error': str(e1)})
            else:
                Category.objects.create(name=name)

            return redirect('category_view_url')
        except Exception as e:
            return render(request, template_name, context={'error': str(e)})


class SubcategoryView(views.View):

    def get(self, request, pk=None):
        template_name = 'admin_function/subcategory.html'
        subcategories = SubCategory.objects.all()
        categories = Category.objects.all()
        context = {'subcategories': subcategories, 'categories': categories}

        if pk:
            subcategory = subcategories.filter(id=pk)

            if str(request.path).endswith('/delete/'):
                context['del_subcategory'] = subcategory[0] if subcategory.exists() else None
            else:
                context['subcategory'] = subcategory[0] if subcategory.exists() else None

        return render(request, template_name, context)

    def post(self, request, pk=None):
        template_name = 'admin_function/subcategory.html'
        try:
            name = request.POST.get('name')
            category_id = request.POST.get('category')

            if pk:
                try:
                    subcategory = SubCategory.objects.get(pk=pk)
                    if str(request.path).endswith('/delete/'):
                        subcategory.delete()
                    else:
                        subcategory.name = name
                        subcategory.category_id = category_id
                        subcategory.save()
                except Exception as e1:
                    return render(request, template_name, context={'error': str(e1)})
            else:
                SubCategory.objects.create(name=name, category_id=category_id)

            return redirect('subcategory_view_url')
        except Exception as e:
            return render(request, template_name, context={'error': str(e)})


class CouponView(views.View):

    def get(self, request, pk=None):
        context = {}

        template_name = 'admin_function/coupon.html'
        coupons = Coupon.objects.all()
        context['coupons'] = coupons

        if pk:
            coupon = coupons.filter(id=pk)

            if str(request.path).endswith('/delete/'):
                context['del_coupon'] = coupon[0] if coupon.exists() else None
            else:
                context['coupon'] = coupon[0] if coupon.exists() else None

        return render(request, template_name, context)

    def post(self, request, pk=None):
        template_name = 'admin_function/coupon.html'
        try:
            # name = request.POST.get('name')
            code = request.POST.get('code')
            start_date = request.POST.get('start_date')
            start_time = request.POST.get('start_time')
            try:
                st_datetime = datetime.datetime.strptime(start_date + ' ' + start_time, '%Y-%m-%d %H:%M')
            except:
                pass
            end_date = request.POST.get('end_date')
            end_time = request.POST.get('end_time')
            try:
                en_datetime = datetime.datetime.strptime(end_date + ' ' + end_time, '%Y-%m-%d %H:%M')
            except:
                pass

            discount_percentage = request.POST.get('discount_percentage')
            minimum_amount = request.POST.get('minimum_amount')
            context = {}
            if pk:
                try:
                    coupon = Coupon.objects.get(pk=pk)
                    if str(request.path).endswith('/delete/'):
                        coupon.delete()
                        return redirect('coupon_view_url')
                    else:
                        coupon.code = code
                        coupon.start_date = st_datetime
                        coupon.expiry_date = en_datetime
                        coupon.discount_percentage = discount_percentage
                        coupon.minimum_amount = minimum_amount
                        coupon.save()
                except Exception as e1:
                    return render(request, template_name, context={'error': str(e1)})
            else:
                Coupon.objects.create(code=code,
                                      start_date=st_datetime, expiry_date=en_datetime,
                                      discount_percentage=discount_percentage,
                                      minimum_amount=minimum_amount)

            return redirect('coupon_view_url')
        except Exception as e:
            raise e
            return render(request, template_name, context={'error': str(e)})


class FontView(views.View):

    def get(self, request, pk=None):
        context = {}

        template_name = 'admin_function/font.html'
        fonts = Font.objects.all()
        context['fonts'] = fonts

        if pk:
            font = fonts.filter(id=pk)

            if str(request.path).endswith('/delete/'):
                context['del_font'] = font[0] if font.exists() else None
            else:
                context['font'] = font[0] if font.exists() else None

        return render(request, template_name, context)

    def post(self, request, pk=None):
        template_name = 'admin_function/font.html'
        try:
            name = request.POST.get('name')
            context = {}
            if pk:

                try:
                    font = Font.objects.get(pk=pk)
                    if str(request.path).endswith('/delete/'):
                        font.delete()
                    else:
                        font.name = name
                        font.save()
                except Exception as e1:
                    return render(request, template_name, context={'error': str(e1)})
            else:
                Font.objects.create(name=name)

            return redirect('font_view_url')
        except Exception as e:
            return render(request, template_name, context={'error': str(e)})


# Owner Functinality

class AddItemView(views.View):

    def get(self, request, pk=None):
        template_name = 'owner_function/add_item.html'

        item_sizes = ItemSize.objects.all()
        colors = Color.objects.all()
        subacategories = SubCategory.objects.all()

        items = Item.objects.all()

        context = {'item_sizes': item_sizes, 'colors': colors, 'subacategories': subacategories, 'items': items}

        if pk:
            item = items.filter(id=pk)

            if str(request.path).endswith('/delete/'):
                context['del_item'] = item[0] if item.exists() else None
            else:
                context['item'] = item[0] if item.exists() else None

        return render(request, template_name, context)

    def post(self, request, pk=None):
        template_name = 'owner_function/add_item.html'
        try:
            name = request.POST.get('name')
            size_id = request.POST.get('size')
            price = request.POST.get('price')
            color_id = request.POST.get('color')
            subcategory_id = request.POST.get('subcategory')

            if pk:

                try:
                    item = Item.objects.get(pk=pk)
                    if str(request.path).endswith('/delete/'):
                        item.delete()
                    else:
                        item.name = name
                        item.item_size_id = size_id
                        item.price = price
                        item.color_id = color_id
                        item.subcategory_id = subcategory_id

                        item.save()
                except Exception as e1:
                    return render(request, template_name, context={'error': str(e1)})
            else:
                Item.objects.create(name=name, price=price, item_size_id=size_id, color_id=color_id,
                                    subcategory_id=subcategory_id)

            return redirect('add_item_url')
        except Exception as e:
            return render(request, template_name, context={'error': str(e)})


# customer Functionality

class CustomerView(views.View):

    def get(self, request, pk=None):
        template_name = 'customer_function/home.html'

        sel_category_id = request.GET.get('category')
        sel_subcategory_id = request.GET.get('subcategory')
        sel_color_id = request.GET.get('color')
        sel_size_id = request.GET.get('size')
        sel_min_price = request.GET.get('min_price')
        sel_max_price = request.GET.get('max_price')

        sel_data = {
            'category': sel_category_id,
            'subcategory': sel_subcategory_id,
            'color': sel_color_id,
            'size': sel_size_id,
            'min_price': sel_min_price,
            'max_price': sel_max_price
        }

        items = Item.objects.all()
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        colors = Color.objects.all()
        sizes = ItemSize.objects.all()

        if sel_category_id:
            items = items.filter(subcategory__category_id=sel_category_id)
        if sel_subcategory_id:
            items = items.filter(subcategory_id=sel_subcategory_id)
        if sel_color_id:
            items = items.filter(color_id=sel_color_id)
        if sel_size_id:
            items = items.filter(size_id=sel_size_id)
        if sel_min_price:
            items = items.filter(price__gte=sel_min_price)
        if sel_max_price:
            items = items.filter(price__lte=sel_max_price)

        context = {'items': items, 'categories': categories,
                   'subcategories': subcategories, 'colors': colors, 'sizes': sizes,
                   'filter_data': sel_data
                   }
        return render(request, template_name, context)

    def post(self, request):
        pass


class BuyView(views.View):
    def get(self, request, item_id):
        template_name = 'customer_function/buy.html'
        item = Item.objects.get(id=item_id)
        fonts = Font.objects.all()
        obj = Item.objects.get(id=item_id)
        price = obj.price
        name = request.user.username
        print(request.user.username)
        adressses = request.user.customer.addresses.all()
        context = {'item': item, 'fonts': fonts, 'name': name, 'adressses': adressses, 'price': price}
        return render(request, template_name, context)

    def post(self, request):
        pass


