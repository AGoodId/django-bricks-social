from django import forms
from django.utils.translation import ugettext as _


from begood.bricks.models import Brick
from begood.bricks.fields import BrickField, BooleanField


FILTER_CHOICES = (
  ('popular', 'popular'),
  ('user', 'user ID'),
  ('tagged', 'tag name'),
  ('location', 'location ID'),
)

SORT_ORDER_CHOICES = (
  ('most-recent', 'most-recent'),
  ('least-recent', 'least-recent'),
  ('most-liked', 'most-liked'),
  ('least-liked', 'least-liked'),
  ('most-commented', 'most-commented'),
  ('least-commented', 'least-commented'),
  ('random', 'random'),
)


class InstagramModuleBrick(Brick):
  """A brick that renders an Instagram feed"""

  template = 'bricks/instagram_module.html'

  client_id = BrickField(_('user ID'), blank=False)
  order_by = BrickField(_('order by'), formfield=forms.ChoiceField(choices=SORT_ORDER_CHOICES), default="most-recent")
  filter_by = BrickField(_('filter by'), formfield=forms.ChoiceField(choices=FILTER_CHOICES), default="popular")
  user_id = BrickField(_('user ID'), blank=True)
  location_id = BrickField(_('location'), blank=True)
  tag_name = BrickField(_('tag name'), blank=True)
  links = BooleanField(_('link to Instagram'), default=True)
  limit = BrickField(_('limit'), formfield=forms.IntegerField(), default=5)
  css_class = BrickField(_('CSS class'), blank=True)

  class Meta:
    proxy = True
    verbose_name = _('Instagram Module')
