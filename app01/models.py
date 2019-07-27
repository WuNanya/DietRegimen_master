from django.db import models

# Create your models here.dietregimen
class User(models.Model):
    user_id = models.AutoField(verbose_name='用户id,主键', primary_key=True)
    user_name = models.CharField(verbose_name='用户名,账号',max_length=32,unique=True)
    password = models.CharField(verbose_name='密码',max_length=32, null=False)
    tel = models.CharField(verbose_name='手机号', max_length=13, null=True)
    email = models.EmailField(verbose_name='邮箱',max_length=32, null=True)
    sex = models.CharField(verbose_name='性别',max_length=3, choices=((1, '男'), (2, '女')), default=1)
    birth = models.DateField(verbose_name='生日',null=True)
    register_time = models.DateTimeField(verbose_name='注册时间',null=False)
    last_login = models.DateTimeField(verbose_name='最后登录时间',null=False)
    # food = models.ManyToManyField()


# 菜品
class Food(models.Model):
    food_id = models.AutoField(verbose_name='菜品id',primary_key=True)
    food_name = models.CharField(verbose_name='菜品名字',max_length=128, null=False, unique=True)
    food_info = models.CharField(verbose_name='菜品介绍',max_length=1024, null=True)    # 菜品描述
    food_make = models.CharField(verbose_name='菜品做法',max_length=2048, null=True)
    food_img = models.CharField(verbose_name='菜品图片',max_length=128, null=True)
    click_num = models.IntegerField(verbose_name='菜品点击数', default=0)
    collect_num = models.IntegerField(verbose_name='菜品收藏量', default=0)


# 食谱
class Menu(models.Model):
    menu_id = models.AutoField(verbose_name='食谱id', primary_key=True)
    user = models.ForeignKey(to='User', to_field='user_id', on_delete=models.CASCADE, null=True)
    menu_name = models.CharField(verbose_name='食谱名称', max_length=64, null=True)


# 标签表
class Tag(models.Model):
    tag_id = models.AutoField(verbose_name='标签id', primary_key=True)
    tag_name = models.CharField(verbose_name='标签名字', max_length=32, unique=True, null=False)
    effective = models.BooleanField(verbose_name='是否有效', default=True)
    click_num = models.IntegerField(verbose_name='标签点击数', null=False, default=0)    # 有人点击自动加一，用于统计热度


# 食谱-标签
class MenuTag(models.Model):
    menu_id = models.ForeignKey(to='Menu', to_field='menu_id', on_delete=models.CASCADE, null=True)
    tag_id = models.ForeignKey(to='Tag', to_field='tag_id', on_delete=models.CASCADE, null=False)
    effective = models.BooleanField(verbose_name='是否有效', default=True)


# 用户收藏表
class Collect(models.Model):
    user = models.ForeignKey(to='User', to_field='user_id', on_delete=models.CASCADE, null=False)
    food = models.ForeignKey(to='Food', to_field='food_id', on_delete=models.CASCADE, null=False)


# 食谱-菜品表
class MenuFood(models.Model):
    menu = models.ForeignKey(to='Menu', to_field='menu_id', on_delete=models.CASCADE, null=False)
    food = models.ForeignKey(to='Food', to_field='food_id', on_delete=models.CASCADE, null=False)


# 菜品标签表
class FoodTag(models.Model):
    food = models.ForeignKey(to='Food', to_field='food_id', on_delete=models.CASCADE, null=False)
    tag = models.ForeignKey(to='Tag', to_field='tag_id', on_delete=models.CASCADE, null=False)


# 历史记录表
class History(models.Model):
    user = models.ForeignKey(to='User', to_field='user_id', on_delete=models.CASCADE, null=False)
    food = models.ForeignKey(to='Food', to_field='food_id', on_delete=models.CASCADE, null=False)
    click_time = models.DateTimeField(verbose_name='用户浏览时间', null=False)


# 用户-标签表
class UserTag(models.Model):
    user = models.ForeignKey(to='User', to_field='user_id', on_delete=models.CASCADE, null=False)
    tag = models.ForeignKey(to='Tag', to_field='tag_id', on_delete=models.CASCADE, null=False)
    click_num = models.IntegerField(verbose_name='标签点击次数', default=0)
    collect_num = models.IntegerField(verbose_name='标签收藏数', default=0)