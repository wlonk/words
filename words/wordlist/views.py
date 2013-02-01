import json

from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404

from .models import Language, Word


def root(request):
    data = {
        'language_json': json.dumps(dict([
            (str(l), l.get_absolute_url()) for l in Language.objects.all()
        ])),
    }
    return render_to_response('root.html', data, mimetype='application/json')


def words(request, iso, count):
    profanity = request.GET.get('profanity', False)
    iso = get_object_or_404(Language, iso=iso)
    count = min(int(count), settings.MAX_WORDS)
    words = Word.objects.filter(
        language=iso,
        profane=profanity
    ).order_by('?')[:count]
    data = {'words': words}
    return render_to_response('words.html', data, mimetype='text/plain')
