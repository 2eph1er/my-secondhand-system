# Generated by Django 4.1.7 on 2023-04-02 02:47

import baykeshop.public.tinymce
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baykeshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baykearticle',
            name='content',
            field=baykeshop.public.tinymce.TinymceField(tinymce={'automatic_uploads': True, 'browser_spellcheck': True, 'contextmenu': False, 'file_picker_types': 'file image media', 'image_title': False, 'images_file_types': 'jpg,svg,webp,png,gif', 'images_reuse_filename': True, 'images_upload_url': '/upload/tinymce/', 'plugins': ['advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak', 'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime', 'media', 'table', 'emoticons', 'template', 'help'], 'toolbar': 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media | forecolor backcolor emoticons'}, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='baykeshopspu',
            name='content',
            field=baykeshop.public.tinymce.TinymceField(tinymce={'automatic_uploads': True, 'browser_spellcheck': True, 'contextmenu': False, 'file_picker_types': 'file image media', 'image_title': False, 'images_file_types': 'jpg,svg,webp,png,gif', 'images_reuse_filename': True, 'images_upload_url': '/upload/tinymce/', 'plugins': ['advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak', 'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime', 'media', 'table', 'emoticons', 'template', 'help'], 'toolbar': 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media | forecolor backcolor emoticons'}, verbose_name='商品详情'),
        ),
    ]
