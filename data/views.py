import json
import base64
from Crypto.Cipher import AES
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from data.models import User, ItemCategory, Shop, Item
from django.conf import settings
from django.core import serializers

# class providing AES Cipher methods
# Not required now since the uesrname and password are stored in its
#   encrypted form in the database, and the received data is also encrypted
#   with the same key.
class AESCipher(object):
    def __init__(self, key):
        self.block_size = 16
        self.cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)

    def _pad(self, s):
        return s +(self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, plain_text):
        plain_text = self._pad(plain_text)
        cipher_text = self.cipher.encrypt(plain_text.encode('utf8'))
        encoded = base64.b64encode(cipher_text)
        return str(encoded, 'utf8')

    def decrypt(self, cipher_text):
        decoded = base64.b64decode(cipher_text)
        plain_text = self.cipher.decrypt(decoded)
        return str(self._unpad(plain_text), 'utf8')


@csrf_exempt
def authenticate_user(request):
    '''
    Receives username and password from request body and
    checks it with the data in the database.

    Returns {"status": "success"} if username and password is found, and
    returns {"status": "failed"} if username or password is not found.
    '''
    request_body = json.loads(request.body)
    username = request_body['username']
    password = request_body['password']
    print(username, password)

    # aes = AESCipher(settings.SECRETS["CRYPT_KEY"])
    # print(aes.decrypt(password))
    # No need to encrypt or decrypt since the data received and the data stored
    # in the database is in encrypted form

    users = User.objects.filter(email=username, password=password)

    if len(users) == 1:
        return HttpResponse(
            '{"status": "success", "id": %d, "email": "%s", "name": "%s"}'
            % (users[0].id, users[0].email, users[0].name),
            status=200
        )

    return HttpResponse('{"status": "failed", "message": "User not found"}', status=200)

@csrf_exempt
def category(request):
    if request.method == 'PUT':
        request_body = json.loads(request.body)
        category_name = request_body['category_name']
        if category_name:
            item_categories = ItemCategory.objects.filter(name=request_body['category_name'])
            if len(item_categories) == 0:
                new_item_category = ItemCategory(name=category_name)
                new_item_category.save()
                return HttpResponse('{"status": "success"}', status=200)
            else:
                return HttpResponse(
                    '{"status": "failed", "message": "Item category already exists"}'
                )
        else:
            return HttpResponse(
                '{"status": "failed", "message": "Invalid item category name"}'
            )
    elif request.method == 'GET':
        item_categories = ItemCategory.objects.all()
        return HttpResponse(serializers.serialize('json', item_categories))
    else:
        return HttpResponse('{"status": "failed", "message": "Invalid request type"}')

@csrf_exempt
def shop(request):
    if request.method == 'PUT':
        request_body = json.loads(request.body)
        shop_name = request_body['shop_name']
        shop_address = request_body['shop_address']
        if shop_name and shop_address:
            shops = Shop.objects.filter(name=shop_name, address=shop_address)
            if len(shops) == 0:
                new_shop = Shop(name=shop_name, address=shop_address)
                new_shop.save()
                return HttpResponse('{"status": "success"}', status=200)
            else:
                return HttpResponse(
                    '{"status": "failed", "message": "Shop already exits"}'
                )
        else:
            return HttpResponse(
                '{"status": "failed", "message": "Invalid shop name or address"}'
            )
    elif request.method == 'GET':
        shops = Shop.objects.all()
        return HttpResponse(serializers.serialize('json', shops), status=200)
    else:
        return HttpResponse('{"status": "failed", "message": "Invalid request type"}')

@csrf_exempt
def item(request):
    if request.method == 'PUT':
        request_body = json.loads(request.body)
        item_name = request_body['name']
        if request_body['name'] and request_body['shop_id']:
            items = Item.objects.filter(name=request_body['name'], shop_id=request_body['shop_id'])
            if len(items) == 0:
                shop = Shop.objects.get(pk=request_body['shop_id'])
                item_category = ItemCategory.objects.get(pk=request_body['category_id'])
                user = User.objects.get(pk=request_body['user_id'])
                if shop and item_category and user:
                    item = Item(
                        shop=shop,
                        category=item_category,
                        user=user,
                        name=request_body['name'],
                        price=request_body['price'],
                        quantity=request_body['quantity'],
                        barcode=request_body['barcode'],
                        quantity_type=request_body['quantity_type'],
                        manufacturer=request_body.get('manufacturer', None),
                        brand=request_body.get('brand', None),
                        manufacturing_date=request_body.get('manufacturing_date', None),
                        expiry_date=request_body.get('expiry_date', None),
                        ingredients=request_body.get('ingredients', None),
                        allergens=request_body.get('allergens', None),
                        remarks=request_body.get('remarks', None),
                        images=request_body['images'],
                    )
                    item.save()
                    return HttpResponse('{"status": "success"}')
                else:
                    return HttpResponse('{"status": "failed", "message": "Invalid data"')
            else:
                return HttpResponse(
                    '{"status": "failed", "message": "Item already exists"}'
                )
        else:
            return HttpResponse(
                '{"status": "failed", "message": "Invalid request body"}'
            )
    else:
        return HttpResponse('{"status": "failed", "message": "Invalid request type"}')
