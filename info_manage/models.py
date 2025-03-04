from django.db import models


class UserInfoModel(models.Model):
    username = models.CharField(max_length=100, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    address = models.CharField(max_length=100, verbose_name='地址')
    phone = models.CharField(max_length=100, verbose_name='手机号')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')

    class Meta:
        db_table = 'db_user_info'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'db_category'
        verbose_name = '类别信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ItemModel(models.Model):
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    name = models.CharField(max_length=100, verbose_name='名称')
    price = models.IntegerField(verbose_name='价格')
    image = models.ImageField(upload_to='', max_length=300, verbose_name='图片')
    content = models.TextField(verbose_name='介绍')
    size = models.CharField(max_length=50, verbose_name='尺寸', default='M')
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, verbose_name='所属分类')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'db_item'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    STATUS_CHOICES = (
        ('ordered', '已下单'),
        ('prepare','备货中'),
        ('unshipped', '待发货'),
        ('shipped', '已发货'),
        ('completed', '已完成'),
    )
    
    item = models.ForeignKey('ItemModel', on_delete=models.CASCADE, verbose_name='所属商品')
    user = models.ForeignKey('UserInfoModel', on_delete=models.CASCADE, verbose_name='所属用户')
    price = models.IntegerField(verbose_name='总价格')
    size = models.CharField(max_length=3, verbose_name='尺寸', default='M')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ordered', verbose_name='订单状态')
    tracking_number = models.CharField(max_length=100, verbose_name='快递单号', blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'db_order'
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item.name


class CarModel(models.Model):
    item = models.ForeignKey('ItemModel', on_delete=models.CASCADE, verbose_name='所属商品')
    user = models.ForeignKey('UserInfoModel', on_delete=models.CASCADE, verbose_name='所属用户')
    price = models.IntegerField(verbose_name='总价格')
    size = models.CharField(max_length=3, verbose_name='尺寸', default='M')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_pay = models.BooleanField(default=False, verbose_name='是否购买')

    class Meta:
        db_table = 'db_car'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item.name


class HotModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    item = models.ForeignKey('ItemModel', on_delete=models.CASCADE, verbose_name='热门商品')

    class Meta:
        db_table = 'db_hot'
        verbose_name = '热门商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CommentModel(models.Model):
    user = models.ForeignKey('UserInfoModel', on_delete=models.CASCADE, verbose_name='所属用户')
    item = models.ForeignKey('ItemModel', on_delete=models.CASCADE, verbose_name='所属商品')
    content = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'db_comment'
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class ItemImageModel(models.Model):
    item = models.ForeignKey('ItemModel', on_delete=models.CASCADE, verbose_name='所属商品')
    image = models.ImageField(upload_to='item_images/', max_length=300, verbose_name='附加图片')
    description = models.CharField(max_length=200, verbose_name='图片描述', blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'db_item_image'
        verbose_name = '商品附加图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.item.name} - 附加图片"
