from django.forms.widgets import Input, TextInput
from django.utils.safestring import mark_safe

class SlugFieldWidget(TextInput):
    """Custom widget that prepopulates from another field"""
    def render(self, name, value, attrs=None):
        i = super(SlugFieldWidget, self).render(name,value,attrs)
        i = i + """
<script type="text/javascript">
    document.getElementById("id_name").onkeyup = function() {
        var e = document.getElementById("id_slug");
        if (!e._changed) { e.value = URLify(document.getElementById("id_name").value, 50); }
    }
</script>
        """# % (name)
        return mark_safe(i)
    class Media:
        js = ('/media/js/slugify.js',)

