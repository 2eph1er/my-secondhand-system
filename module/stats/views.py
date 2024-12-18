

from django.core.cache import cache
from django.utils import timezone
from django.db.models import F
from django.contrib.contenttypes.models import ContentType

from baykeshop.config.settings import bayke_settings
from baykeshop.models import BaykeIPAddress, BaykeStats


class BaykeStatsMixins:
    """ 数据统计类 
    from baykeshop.module.stats.views import BaykeStatsMixins
    stats_cls = BaykeStatsMixins(request)
    stats = stats_cls.get_stats(model, object_id)  model要统计的模型类, 要统计的对象id(int类型)
    pv = stats.pv
    uv = stats.uv
    """
    def __init__(self, request) -> None:
        self.request = request
        self.user = request.user
    
    def get_user_ip(self):
        meta = self.request.META
        ip = meta.get('HTTP_X_FORWARDED_FOR', meta['REMOTE_ADDR'])
        return ip
    
    def get_stats(self, model, object_id:int):
        # 获取当前模型的浏览量和访问量
        increase_pv = False
        increase_uv = False
        ip = self.get_user_ip()
        
        pv_key = 'pv:%s:%s:%s' % (ip, self.request.path, object_id)
        uv_key = 'uv:%s:%s:%s:%s' % (ip, str(timezone.now().date()), self.request.path, object_id)
        
        content_type = ContentType.objects.get_for_model(model=model)
        
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key, 1, bayke_settings.PV_TIMEOUT)  # 1分钟有效
            
        if not cache.get(uv_key):
            increase_uv = True
            cache.set(uv_key, 1, bayke_settings.UV_TIMEOUT)  # 24小时有效
        
        stats = BaykeStats.objects.filter(content_type=content_type, object_id=object_id)
        if stats.exists():
            if increase_pv and increase_uv:
                stats.update(pv=F('pv')+1, uv=F('uv')+1)
                BaykeIPAddress.objects.create(ip=ip, browser=self.request.headers['User-Agent'])
            elif increase_pv:
                stats.update(pv=F('pv')+1)
            elif increase_uv:
                BaykeIPAddress.objects.create(ip=ip, browser=self.request.headers['User-Agent'])
                stats.update(uv=F('uv')+1)
        else:
            BaykeStats.objects.create(content_type=content_type, object_id=object_id, pv=1, uv=1)
        return stats.first()
  
