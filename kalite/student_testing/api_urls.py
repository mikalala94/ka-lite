from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('student_testing.api_views',
    url(r'save_attempt_log$', 'save_attempt_log', {}, 'save_attempt_log'),
)