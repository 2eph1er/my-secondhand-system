#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.core import management
from django.conf import settings

from baykeshop.models import BaykePermission, BaykeMenu


class Command(BaseCommand):
    help = '初始化后台管理菜单以及导入测试数据'
    
    def add_arguments(self, parser):
        parser.add_argument('-test', '--test', action='store_true', help="导入演示数据")
        
    def handle(self, *args, **options):
        menus_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykemenu.json"
        management.call_command('loaddata', menus_json, verbosity=0)
        menus = BaykeMenu.objects.all()
        perms = Permission.objects.all() 
        for perm in perms:
            if perm.codename in ['view_baykeshopcategory', 'view_baykeshopspec', 'view_baykeshopspu', 'view_baykebanner']:
                BaykePermission.objects.update_or_create(permission=perm, menus=menus.filter(name="商城").first(), defaults={'permission': perm})
            elif perm.codename in ['view_group', 'view_user', 'view_baykemenu', 'view_logentry']:
                BaykePermission.objects.update_or_create(permission=perm, menus=menus.filter(name="认证和授权").first(), defaults={'permission': perm})
            elif perm.codename in ['view_baykeshoporderinfo']:
                BaykePermission.objects.update_or_create(permission=perm, menus=menus.filter(name="订单").first(), defaults={'permission': perm})
            elif perm.codename in ['view_flatpage', 'view_site', 'view_baykearticle', 'view_baykearticlecategory']:
                BaykePermission.objects.update_or_create(permission=perm, menus=menus.filter(name="内容").first(), defaults={'permission': perm})
                flatpage_json = f"{settings.BASE_DIR}/baykeshop/config/db/flatpage.json"
                management.call_command('loaddata', flatpage_json, verbosity=0)
        self.stdout.write(self.style.SUCCESS('Successfully "%s"' % 'push baykeadmin menus'))
        
        if options['test']:
            banners_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykebanner.json"
            management.call_command('loaddata', banners_json, verbosity=0)
            category_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykeshopcategory.json"
            management.call_command('loaddata', category_json, verbosity=0)
            
            spec_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykeshopspec.json"
            specoption_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykeshopspecoption.json"
            spu_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykeshopspu.json"
            spucarousel_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykespucarousel.json"
            sku_json = f"{settings.BASE_DIR}/baykeshop/config/db/baykeshopsku.json"
            # flatpage_json = f"{settings.BASE_DIR}/baykeshop/config/db/flatpage.json"
            
            management.call_command('loaddata', spec_json, verbosity=0)
            management.call_command('loaddata', specoption_json, verbosity=0)
            management.call_command('loaddata', spu_json, verbosity=0)
            management.call_command('loaddata', spucarousel_json, verbosity=0)
            management.call_command('loaddata', sku_json, verbosity=0)
            # management.call_command('loaddata', flatpage_json, verbosity=0)
            self.stdout.write(self.style.SUCCESS('Successfully "%s"' % 'push baykeshop test data'))
        