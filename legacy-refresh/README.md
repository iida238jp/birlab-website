# BIRLab public-site static clone

This directory is an experimental static clone of the public website at
<https://birlab.org/>. It preserves the live site's page structure, published
content, navigation, styling, and locally hosted media as a safe base for a
future “original-site-structure, updated-content” redesign.

- Captured: 23 August 2026
- Scope: the public home page, public pages listed in the site's sitemap,
  same-domain pages reached through their navigation, public research and event
  pages, and same-site assets required to render them
- Included: 27 static HTML pages and 170 locally stored supporting assets
- External media: YouTube, Vimeo, WordPress Video, and other third-party media
  remain embeds or external links; their video files were not copied
- Excluded: WordPress administration and login routes, authentication-only or
  password-protected content, APIs, search-result generation, feeds,
  trackbacks, comment submission, subscriptions, and crawling of external sites

## Static-clone limitations

WordPress-specific server features do not work in this clone. Search, comments,
subscriptions, login, administration, and server-side form processing are
disabled or excluded. Forms retain their visual presentation where practical
but cannot submit. Four download links on the source Resources page already
returned HTTP 404 at capture time and are marked unavailable in this clone.

Every cloned HTML page contains `noindex, nofollow` so that this experimental
copy is not indexed as the canonical BIRLab site. Internal page and asset links
have been made relative so the clone works from a repository subdirectory.

All future content updates and redesign experiments based on this snapshot must
remain inside `legacy-refresh/`. The repository root site, its assets, its
deployment workflow, and the live <https://birlab.org/> site were not changed by
this capture.
