---
layout: page
title: Meeting Notes
subtitle: Check What Happened This Week!
---
<div class="posts-list">{% for post in paginator.posts %}

<article class="post-preview">[

## {{ post.title }}

{% if post.subtitle %}

### {{ post.subtitle }}

{% endif %}]({{ post.url | prepend: site.baseurl }})

Posted on {{ post.date | date: "%B %-d, %Y" }}

<div class="post-entry-container">{% if post.image %}

<div class="post-image">[![]({{ post.image }})]({{ post.url | prepend: site.baseurl }}) </div>

{% endif %}

<div class="post-entry">{{ post.excerpt | strip_html | xml_escape | truncatewords: site.excerpt_length }} {% assign excerpt_word_count = post.excerpt | number_of_words %} {% if post.content != post.excerpt or excerpt_word_count > site.excerpt_length %} [[Read More]]({{ post.url | prepend: site.baseurl }}) {% endif %}</div>

</div>

{% if post.tags.size > 0 %}

<div class="blog-tags">Tags: {% if site.link-tags %} {% for tag in post.tags %} [{{- tag -}}]({{ site.baseurl }}/tags#{{- tag -}}) {% endfor %} {% else %} {{ post.tags | join: ", " }} {% endif %}</div>

{% endif %}</article>

{% endfor %}</div>

{% if paginator.total_pages > 1 %}

*   [← Newer Posts]({{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }})

*   [Older Posts →]({{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }})

{% endif %}
