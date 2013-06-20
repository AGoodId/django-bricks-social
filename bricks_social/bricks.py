from django import forms
from django.utils.translation import ugettext as _


from begood.bricks.models import Brick
from begood.bricks.fields import BrickField, BooleanField


FB_COLOR_SCHEME_CHOICES = (
  ('light', 'light'),
  ('dark', 'dark'),
)

INSTAGRAM_FILTER_CHOICES = (
  ('popular', 'popular'),
  ('user', 'user ID'),
  ('tagged', 'tag name'),
  ('location', 'location ID'),
)

INSTAGRAM_SORT_ORDER_CHOICES = (
  ('most-recent', 'most-recent'),
  ('least-recent', 'least-recent'),
  ('most-liked', 'most-liked'),
  ('least-liked', 'least-liked'),
  ('most-commented', 'most-commented'),
  ('least-commented', 'least-commented'),
  ('random', 'random'),
)


class FBLikeBoxBrick(Brick):
  """A brick that renders an Instagram feed"""

  template = 'bricks/fb_like_box.html'

  page_url = BrickField(_('Facebook Page URL'), blank=False)
  width = BrickField(_('limit'), formfield=forms.IntegerField(), default=300)
  height = BrickField(_('limit'), formfield=forms.IntegerField(), blank=True)
  show_faces = BooleanField(_('show faces'), default=True)
  show_header = BooleanField(_('show header'), default=False)
  show_stream = BooleanField(_('show stream'), default=False)
  show_border = BooleanField(_('show border'), default=False)
  color_scheme = BrickField(_('color scheme'), formfield=forms.ChoiceField(choices=FB_COLOR_SCHEME_CHOICES), default="light")
  css_class = BrickField(_('CSS class'), blank=True)

  class Meta:
    proxy = True
    verbose_name = _('Facebook Like Box')


class InstagramModuleBrick(Brick):
  """A brick that renders an Instagram feed"""

  template = 'bricks/instagram_module.html'

  client_id = BrickField(_('user ID'), blank=False)
  order_by = BrickField(_('order by'), formfield=forms.ChoiceField(choices=INSTAGRAM_SORT_ORDER_CHOICES), default="most-recent")
  filter_by = BrickField(_('filter by'), formfield=forms.ChoiceField(choices=INSTAGRAM_FILTER_CHOICES), default="popular")
  user_id = BrickField(_('user ID'), blank=True)
  location_id = BrickField(_('location'), blank=True)
  tag_name = BrickField(_('tag name'), blank=True)
  links = BooleanField(_('link to Instagram'), default=True)
  limit = BrickField(_('limit'), formfield=forms.IntegerField(), default=5)
  css_class = BrickField(_('CSS class'), blank=True)

  class Meta:
    proxy = True
    verbose_name = _('Instagram Module')


class TwitterWidgetBrick(Brick):
  """A brick that renders a Twitter Widget"""

  template = 'bricks/twitter_widget.html'

  embed_code = BrickField(_('embed code'), formfield=forms.CharField(widget=forms.Textarea(attrs={'rows': 25})))
  css_class = BrickField(_('CSS class'), blank=True)
