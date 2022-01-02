For this app's bug #2198, there are two different bug-triggering traces, which lead to two slightly different crash stacks (these two traces may mean two different bugs but we are not sure)
In our study, we choose the medium-difficult bug-triggering trace (see the video file "video-#2198-medium.mp4") because
the other trace is trivial (see the video file "video-#2198-easy.mp4") which we assume it may not be a good candidate for
evaluating GUI testing tools.

From the stack trace, the only difference between these two bugs is (non-instrumented apk):
[video-#2198-medium.mp4]: org.fossasia.openevent.general.search.SearchFilterFragment$setFilters$3.onClick(SearchFilterFragment.kt:127)
[video-#2198-easy.mp4]: org.fossasia.openevent.general.search.SearchFragment$onCreateView$3.onClick(SearchFragment.kt:94)

However, when we instrumented the apk, the stack traces change a bit:
[video-#2198-medium.mp4]: org.fossasia.openevent.general.search.SearchFilterFragment$setFilters$3.onClick(SearchFilterFragment.kt:134)
[video-#2198-easy.mp4]: org.fossasia.openevent.general.search.SearchFragment$onCreateView$3.onClick(SearchFragment.kt:95)

In scripts/check_crash.py, we focus on checking [video-#2198-medium.mp4] and explicitly use the line number in the stack trace to differ two different bugs.

For this bug, it is not easy to check whether ComboDroid can find the bug or not. Because ComboDroid discards the line numbers when it instruments the APK by itself. It means even if  ComboDroid can find this bug, the key line in the stack trace will only be: 'org.fossasia.openevent.general.search.SearchFilterFragment$setFilters$3.onClick(SearchFilterFragment.kt)',