# This file aims to do quick crash checking. 
# Note that this file applies to both the instrumented and non-intrumented APKs for most bugs 
#   because we ignore the concrete line numbers in the stack traces. 
# But for some specific bugs of WordPress (i.e., WordPress-#11135/#10547/#10363), this file only applies to the
#   corresponding intrumented APKs because these bugs are forward-ported (i.e. the app source code may has changed
#   and as a result, the stack traces may also have changed).

import csv
import datetime
import os
import shutil
import subprocess
import time
from argparse import ArgumentParser, Namespace
from typing import List, Dict, Set

ALL_APPS = ['ActivityDiary', 'AmazeFileManager', 'and-bible', 'AnkiDroid', 'APhotoManager', 'commons',
            'collect', 'FirefoxLite', 'Frost', 'geohashdroid', 'MaterialFBook', 'nextcloud', 'Omni-Notes',
            'open-event-attendee-android', 'openlauncher', 'osmeditor4android', 'Phonograph', 'Scarlet-Notes',
            'sunflower', 'WordPress']

app_crash_data = {

    'AnkiDroid': {

        '#4200': ['com.ichi2.libanki.Note com.ichi2.libanki.Card.note()',
                  'com.ichi2.async.DeckTask.doInBackgroundUpdateNote(DeckTask.java',
                  'com.ichi2.async.DeckTask.doInBackground(DeckTask.java'],

        '#4451': [
            'android.support.design.widget.CoordinatorLayout$LayoutParams cannot be cast to android.widget.RelativeLayout$LayoutParams',
            'com.ichi2.anki.AbstractFlashcardViewer.initLayout(AbstractFlashcardViewer.java',
            'com.ichi2.anki.AbstractFlashcardViewer.onCollectionLoaded(AbstractFlashcardViewer.java',
            'com.ichi2.anki.Reviewer.onCollectionLoaded(Reviewer.java',
            'com.ichi2.anki.AnkiActivity.onLoadFinished(AnkiActivity.java'],

        '#5638': ['com.ichi2.libanki.Utils.stripHTMLMedia'],

        '#4707': ['exposed beyond app through ClipData.Item.getUri()',
                  'com.ichi2.anki.AnkiActivity.startActivityForResult(AnkiActivity.java',
                  'com.ichi2.anki.multimediacard.fields.BasicImageFieldController$2.onClick(BasicImageFieldController.java'],

        '#6145': ['com.ichi2.libanki.AnkiPackageExporter.exportInto(AnkiPackageExporter.java'],

        '#5756': ['Unable to start activity ComponentInfo{com.ichi2.anki/com.ichi2.anki.Reviewer}',
                  'com.ichi2.anki.AbstractFlashcardViewer.restoreCollectionPreferences(AbstractFlashcardViewer.java',
                  'com.ichi2.anki.AbstractFlashcardViewer.onCollectionLoaded(AbstractFlashcardViewer.java',
                  'com.ichi2.anki.AnkiActivity.startLoadingCollection(AnkiActivity.java'],

        '#4977': [
            "Attempt to invoke virtual method 'boolean android.support.v7.widget.SearchView.isIconified()' on a null object reference",
            'com.ichi2.anki.CardBrowser$20.onPostExecute(CardBrowser.java',
            'com.ichi2.async.DeckTask$TaskListener.onPostExecute(DeckTask.java',
            'com.ichi2.async.DeckTask.onPostExecute(DeckTask.java']
    },

    'ActivityDiary': {

        '#118': ['java.lang.IllegalArgumentException: position (',
                 'de.rampro.activitydiary.ui.generic.DetailRecyclerViewAdapter.getDiaryImageIdAt(DetailRecyclerViewAdapter.java',
                 'de.rampro.activitydiary.ui.history.HistoryRecyclerViewAdapter'],

        '#285': ['java.lang.NumberFormatException: For input string',
                 'de.rampro.activitydiary.ui.settings.SettingsActivity.updateLocationAge(SettingsActivity.java',
                 'de.rampro.activitydiary.ui.settings.SettingsActivity.onSharedPreferenceChanged(SettingsActivity.java']
    },

    'geohashdroid': {

        '#73': ['java.lang.RuntimeException: An error occurred while executing doInBackground()',
                'java.lang.String net.exclaimindustries.geohashdroid.util.Graticule.getLatitudeString(boolean)',
                'net.exclaimindustries.geohashdroid.util.HashBuilder$StockRunner.runStock(HashBuilder.java',
                'net.exclaimindustries.geohashdroid.services.StockService.onHandleWork(StockService.java']
    },

    'and-bible': {

        '#261': ['java.lang.StackOverflowError: stack size',
                 'org.crosswire.jsword.index.lucene.LuceneIndex.generateSearchIndexImpl(LuceneIndex.java'],

        '#375': ["kotlin.TypeCastException: null cannot be cast to non-null type org.crosswire.jsword.book.Book",
                 "net.bible.service.history.HistoryManager.setDumpString(HistoryManager.kt",
 	             "net.bible.android.control.page.window.WindowRepository.restoreState(WindowRepository.kt",
 	             "net.bible.android.view.activity.page.MainBibleActivity.openTab(MainBibleActivity.kt",
 	             "net.bible.android.view.activity.page.MainBibleActivity.access$openTab(MainBibleActivity.kt",
 	             "net.bible.android.view.activity.page.MainBibleActivity$chooseTab$1.onClick(MainBibleActivity.kt"
                 ],

        '#480': ['net.bible.service.db.bookmark.BookmarkDBAdapter.updateLabel(BookmarkDBAdapter.kt',
                 'net.bible.android.control.bookmark.BookmarkControl.saveOrUpdateLabel(BookmarkControl.kt',
                 'net.bible.android.view.activity.bookmark.LabelDialogs$1.onClick(LabelDialogs.java'],

        '#697': [
            'Unable to start activity ComponentInfo{net.bible.android.activity/net.bible.android.view.activity.mynote.MyNotes}',
            'net.bible.android.control.versification.sort.VersificationPrioritiser.getVersifications(VersificationPrioritiser.java',
            'net.bible.android.control.versification.sort.ConvertibleVerseRangeComparator$Builder.withMyNotes(ConvertibleVerseRangeComparator.java'],

        '#703': ["java.lang.NullPointerException: Attempt to invoke interface method 'org.crosswire.jsword.index.IndexStatus org.crosswire.jsword.book.Book.getIndexStatus()' on a null object reference",
                 "net.bible.android.view.activity.search.SearchIndexProgressStatus.jobFinished(SearchIndexProgressStatus.java",
                 "net.bible.android.view.activity.base.ProgressActivityBase.updateProgress(ProgressActivityBase.kt",
                 "net.bible.android.view.activity.base.ProgressActivityBase$initialiseView$uiUpdaterRunnable$1.run(ProgressActivityBase.kt"
                 ]
    },

    'AmazeFileManager': {

        '#1232': ['Failure delivering result ResultInfo',
                  "Attempt to invoke virtual method 'java.lang.Object java.util.ArrayList.get(int)' on a null object reference",
                  'com.amaze.filemanager.activities.MainActivity.onActivityResult(MainActivity.java',
                  ],
        '#1558': ["com.amaze.filemanager.exceptions.StreamNotFoundException: Can't get stream",
                  "com.amaze.filemanager.filesystem.FileUtil.getOutputStream(FileUtil.java",
                  "com.amaze.filemanager.filesystem.FileUtil.isWritable(FileUtil.java",
                  'com.amaze.filemanager.asynchronous.asynctasks.WriteFileAbstraction.doInBackground'],

        '#1796': ["java.lang.IndexOutOfBoundsException: Index:",
                  'com.amaze.filemanager.asynchronous.asynctasks.DeleteTask.onPostExecute(DeleteTask.java'],

        '#1837': ['java.lang.IndexOutOfBoundsException: Index:',
                  'com.amaze.filemanager.adapters.glide.RecyclerPreloadModelProvider.getPreloadItems(RecyclerPreloadModelProvider.java',
                  'com.bumptech.glide.ListPreloader.preload(ListPreloader.java',
                  'com.bumptech.glide.integration.recyclerview.RecyclerToListViewScrollListener.onScrolled(RecyclerToListViewScrollListener.java']
    },

    'FirefoxLite': {

        '#4881': ["java.lang.NullPointerException: Attempt to invoke virtual method 'void android.view.View.setVisibility(int)' on a null object reference",
                  "org.mozilla.rocket.content.common.ui.ContentTabHelper$Observer.onEnterFullScreen(ContentTabHelper.kt",
                  "org.mozilla.rocket.tabs.TabViewEngineObserver$onEnterFullScreen$1.invoke(TabViewEngineObserver.kt",
                  "mozilla.components.support.base.observer.ObserverRegistry.notifyObservers(ObserverRegistry.kt",
                  "at org.mozilla.rocket.tabs.Session.notifyObservers(Session.kt)",
                  "at org.mozilla.rocket.tabs.TabViewEngineObserver.onEnterFullScreen(TabViewEngineObserver.kt",
                  "at org.mozilla.rocket.tabs.TabViewEngineSession$ChromeClient$onEnterFullScreen$1.invoke(TabViewEngineSession.kt",
                  "at org.mozilla.rocket.tabs.TabViewEngineSession$ChromeClient$onEnterFullScreen$1.invoke(TabViewEngineSession.kt",
                  "at mozilla.components.support.base.observer.ObserverRegistry.notifyObservers(ObserverRegistry.kt",
                  "at org.mozilla.rocket.tabs.TabViewEngineSession.notifyObservers(TabViewEngineSession.kt)",
                  "at org.mozilla.rocket.tabs.TabViewEngineSession$ChromeClient.onEnterFullScreen(TabViewEngineSession.kt",
                  "at org.mozilla.focus.webkit.FocusWebChromeClient.onShowCustomView(FocusWebChromeClient.java"
                  ],

        '#4942': [
            'java.lang.RuntimeException: Cannot create an instance of class org.mozilla.rocket.home.HomeViewModel',
            'java.lang.InstantiationException: java.lang.Class<org.mozilla.rocket.home.HomeViewModel> has no zero argument constructor',
            'org.mozilla.focus.tabs.tabtray.TabTrayFragment.onCreateView(TabTrayFragment.java'],

        '#5085': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.os.BaseBundle.getString(java.lang.String)' on a null object reference",
            'org.mozilla.focus.settings.SettingsFragment.onCreate(SettingsFragment.kt']

    },

    'open-event-attendee-android': {
        '#2198': [
            "androidx.fragment.app.Fragment$InstantiationException: Unable to instantiate fragment org.fossasia.openevent.general.search.type.SearchTypeFragment: calling Fragment constructor caused an exception",
            # for instrumented apk
            "org.fossasia.openevent.general.search.SearchFilterFragment$setFilters$3.onClick(SearchFilterFragment.kt:134)",
            # for non-instrumented apk
            #   "org.fossasia.openevent.general.search.SearchFilterFragment$setFilters$3.onClick(SearchFilterFragment.kt:127)"
            "org.fossasia.openevent.general.search.type.SearchTypeFragment.<init>(SearchTypeFragment.kt"
            ]
    },

    'openlauncher': {
        '#67': ['java.lang.SecurityException: Not allowed to change Do Not Disturb state',
                'com.benny.openlauncher.util.LauncherAction.RunAction(LauncherAction.java',
                'com.benny.openlauncher.activity.Home$11.onItemClick(Home.java']
    },

    'APhotoManager': {
        '#116': ['Error inflating class de.k3b.android.widgets.EditTextPreferenceWithSummary',
                 'de.k3b.android.androFotoFinder.SettingsActivity.onCreate(SettingsActivity.java']
    },

    'sunflower': {
        '#239': [
            'java.lang.IllegalArgumentException: navigation destination com.google.samples.apps.sunflower:id/action_plant_list_fragment_to_plant_detail_fragment is unknown to this NavController',
            'com.google.samples.apps.sunflower.adapters.PlantAdapter$createOnClickListener$1.onClick(PlantAdapter.kt']
    },

    'collect': {
        '#3222': ["java.lang.IllegalArgumentException: column 'MAX(date)' does not exist",

                  'org.odk.collect.android.activities.FormChooserList.onLoadFinished(FormChooserList.java']
    },

    'MaterialFBook': {
        '#224': ['android.content.res.Resources$NotFoundException: Resource ID #0x20b001b',
                 'org.chromium.ui.base.DeviceFormFactor.b(PG',
                 'org.chromium.ui.base.DeviceFormFactor.a(PG',
                 'bCE.onCreateActionMode(PG',
                 'org.chromium.content.browser.selection.SelectionPopupControllerImpl.y(PG',
                 'org.chromium.content.browser.selection.SelectionPopupControllerImpl.showSelectionMenu(PG']
    },

    'Omni-Notes': {
        '#745': ["it.feio.android.omninotes.alpha",
                 "java.lang.NoSuchMethodError: No virtual method fitCenter()Lcom/bumptech/glide/request/RequestOptions; in class Lcom/bumptech/glide/request/RequestOptions; or its super classes (declaration of 'com.bumptech.glide.request.RequestOptions' appears in",
                 "it.feio.android.simplegallery.GalleryPagerFragment.onCreateView(GalleryPagerFragment.java"]
    },

    'Phonograph': {
        '#112': ['com.kabouzeid.gramophone.appshortcuts.AppShortcutLauncherActivity.startServiceWithSongs']
    },

    'osmeditor': {
        '#637': ["java.lang.NullPointerException: Attempt to invoke interface method 'java.util.Set java.util.Map.entrySet()' on a null object reference",
            "de.blau.android.validation.BaseValidator.validateElement(BaseValidator.java",
            "de.blau.android.validation.BaseValidator.validate(BaseValidator.java",
            "de.blau.android.osm.Way.validate(Way.java",
            "de.blau.android.osm.OsmElement.hasProblem(OsmElement.java",
            "de.blau.android.Map.paintWay(Map.java",
            "de.blau.android.Map.paintOsmData(Map.java",
            "de.blau.android.Map.onDraw(Map.java"
            ],

        # '#705': [
        #    "android.view.ViewRootImpl$CalledFromWrongThreadException: Only the original thread that created a view hierarchy can touch its views",
        #    "de.blau.android.propertyeditor.PresetFragment$3.doInBackground(PresetFragment.java:258)",
        #    "de.blau.android.propertyeditor.PresetFragment$3.doInBackground(PresetFragment.java:244)"],

        '#729': [
            "java.lang.RuntimeException: An error occurred while executing doInBackground()",
            "android.view.ViewRootImpl$CalledFromWrongThreadException: Only the original thread that created a view hierarchy can touch its views",
            "de.blau.android.propertyeditor.PresetFragment$3.doInBackground(PresetFragment.java",
            "de.blau.android.propertyeditor.PresetFragment$3.doInBackground(PresetFragment.java"]
    },

    'Scarlet-Notes': {
        '#114': ['java.lang.Exception: Invalid Search Mode',
                 'com.maubis.scarlet.base.support.SearchConfigKt.getNotesForMode(SearchConfig.kt',
                 'com.maubis.scarlet.base.support.SearchConfigKt.filterSearchWithoutFolder(SearchConfig.kt',
                 'com.maubis.scarlet.base.support.SearchConfigKt.unifiedSearchSynchronous(SearchConfig.kt',
                 'com.maubis.scarlet.base.MainActivity$unifiedSearchSynchronous$$inlined$map$lambda$1.invokeSuspend(MainActivity.kt']

    },

    'Frost': {

        '#1323': [
            "java.net.UnknownHostException: Unable to resolve host \"m.facebook.com\": No address associated with hostname",
            "com.pitchedapps.frost.fragments.FrostParserFragment.reloadImpl$suspendImpl(RecyclerFragmentBase.kt",
            "com.pitchedapps.frost.fragments.FrostParserFragment.reloadImpl(RecyclerFragmentBase.kt)",
            "com.pitchedapps.frost.fragments.RecyclerFragment$reload$2.invokeSuspend(RecyclerFragmentBase.kt"]
    },

    'commons': {
        '#1385': ['java.lang.NullPointerException: Callable returned null'],
        '#1391': ["fr.free.nrw.commons.nearby.NearbyMapFragment$8.onStateChanged(NearbyMapFragment.java"],

        '#1581': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'double android.location.Location.getLatitude()' on a null object reference",
            "fr.free.nrw.commons.location.LatLng.from(LatLng.java",
            'fr.free.nrw.commons.location.LocationServiceManager.getLKL(LocationServiceManager.java',
            'fr.free.nrw.commons.nearby.NearbyActivity.onRequestPermissionsResult(NearbyActivity.java',
            'fr.free.nrw.commons.nearby.NearbyActivity.onRequestPermissionsResult(NearbyActivity.java'],

        '#2123': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'android.support.v4.app.FragmentActivity android.support.v4.app.Fragment.getActivity()' on a null object reference",
            'fr.free.nrw.commons.media.MediaDetailPagerFragment$MediaDetailAdapter.getItem(MediaDetailPagerFragment.java'],
        '#3244': ['fr.free.nrw.commons.upload.UploadActivity.receiveInternalSharedItems(UploadActivity.java']
    },

    'nextcloud': {
        '#1918': [
            'java.lang.ClassCastException: com.owncloud.android.ui.preview.PreviewImageActivity cannot be cast to com.owncloud.android.ui.activity.FileDisplayActivity',
            'com.owncloud.android.ui.preview.PreviewImageFragment.onOptionsItemSelected(PreviewImageFragment.java'],

        '#4026': [
            'java.lang.RuntimeException: Unable to start activity ComponentInfo{com.nextcloud.client/com.owncloud.android.ui.activity.FileDisplayActivity}',
            'com.owncloud.android.ui.activity.ToolbarActivity.setupToolbar(ToolbarActivity.java',
            'com.owncloud.android.ui.activity.FileDisplayActivity.onCreate(FileDisplayActivity.java'],

        '#4792': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String com.owncloud.android.datamodel.OCFile.getRemotePath()' on a null object reference",
            'com.owncloud.android.ui.dialog.CreateFolderDialogFragment.onClick(CreateFolderDialogFragment.java'],

        '#5173': ['android.view.MenuItem android.view.MenuItem.setVisible(boolean)',
                  'com.owncloud.android.ui.fragment.OCFileListFragment.onPrepareOptionsMenu(OCFileListFragment.java']
    },

    'WordPress': {

        '#6530': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'void org.wordpress.android.fluxc.model.PostModel.setDateLocallyChanged(java.lang.String)' on a null object reference",
            "org.wordpress.android.fluxc.store.PostStore.updatePost(PostStore.java",
            "org.wordpress.android.fluxc.store.PostStore.onAction(PostStore.java"
            ],

        '#7182': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'void org.wordpress.android.ui.accounts.SmartLockHelper.saveCredentialsInSmartLock(java.lang.String, java.lang.String, java.lang.String, android.net.Uri)' on a null object reference",
            "org.wordpress.android.ui.accounts.LoginActivity.saveCredentialsInSmartLock(LoginActivity.java",
            "org.wordpress.android.login.LoginBaseFormFragment.saveCredentialsInSmartLock(LoginBaseFormFragment.java",
            "org.wordpress.android.login.LoginUsernamePasswordFragment.finishLogin(LoginUsernamePasswordFragment.java",
            "org.wordpress.android.login.LoginUsernamePasswordFragment.onSiteChanged(LoginUsernamePasswordFragment.java"
            ],
            
        '#8659': [
            'Two different ViewHolders have the same stable ID. Stable IDs in your adapter MUST BE unique and SHOULD NOT change.'],

        # forward-ported 
        '#10302': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String org.wordpress.android.fluxc.model.SiteModel.getMobileEditor()' on a null object reference",
            "org.wordpress.android.util.SiteUtils.isBlockEditorDefaultForNewPost(SiteUtils.java",
            "org.wordpress.android.ui.accounts.HelpActivity$Companion.createIntent(HelpActivity.kt",
            "org.wordpress.android.ui.accounts.HelpActivity.createIntent(HelpActivity.kt)",
            "org.wordpress.android.ui.ActivityLauncher.viewHelpAndSupport(ActivityLauncher.java",
            "org.wordpress.android.ui.accounts.LoginActivity.viewHelpAndSupport(LoginActivity.java",
            "org.wordpress.android.ui.accounts.LoginActivity.helpEmailScreen(LoginActivity.java",
            "org.wordpress.android.login.LoginEmailFragment.onHelp(LoginEmailFragment.java",
            "org.wordpress.android.login.LoginBaseFormFragment.onOptionsItemSelected(LoginBaseFormFragment.java"],

        # forward-ported 
        '#10363': ["java.lang.NullPointerException: itemView.findViewById(R.id.container) must not be null",
                   "org.wordpress.android.ui.posts.PostListItemViewHolder.<init>(PostListItemViewHolder.kt",
                   "org.wordpress.android.ui.posts.PostListItemViewHolder$Compact.<init>(PostListItemViewHolder.kt",
                   "org.wordpress.android.ui.posts.adapters.PostListAdapter.onCreateViewHolder(PostListAdapter.kt"
                   ],

        # forward-ported 
        '#10547': [
            "java.lang.RuntimeException: Unable to start activity ComponentInfo{org.wordpress.android/org.wordpress.android.ui.posts.EditPostActivity}: java.lang.RuntimeException: PostLoadingState wrong value 6",
            "org.wordpress.android.ui.posts.editor.PostLoadingState$Companion.fromInt(PostLoadingState.kt",
            "org.wordpress.android.ui.posts.editor.PostLoadingState.fromInt(PostLoadingState.kt)",
            "org.wordpress.android.ui.posts.EditPostActivity.onCreate(EditPostActivity.java"
        ],

        '#10876': ['in WithSelect(WithDispatch(WithViewportMatch(WithPreferredColorScheme(Component))))'],

        # forward-ported 
        '#11135': [
            "java.lang.NullPointerException",
            "org.wordpress.android.ui.CommentFullScreenDialogFragment.onCreateView(CommentFullScreenDialogFragment.kt",
            "org.wordpress.android.ui.CollapseFullScreenDialogFragment.onActivityCreated(CollapseFullScreenDialogFragment.java"],

        '#11992': [
            "java.lang.NullPointerException: Attempt to invoke virtual method 'boolean org.wordpress.android.ui.FilteredRecyclerView.isRefreshing()' on a null object reference",
            'org.wordpress.android.ui.reader.ReaderPostListFragment.onSaveInstanceState(ReaderPostListFragment.java']
    }
}


def get_testing_result_dir(all_testing_result_dirs, app_name, issue_id):
    tmp_paths = []
    for result_dir_path in all_testing_result_dirs:
        result_dir_basename = os.path.basename(result_dir_path)
        if app_name in result_dir_basename and issue_id in result_dir_basename:
            tmp_paths.append(result_dir_path)
    return tmp_paths


def get_app_name(testing_result_dir):
    for app_name in ALL_APPS:
        if os.path.basename(testing_result_dir).startswith(app_name):
            return app_name
    print("Warning: cannot find app name for this testing result dir: %s" % testing_result_dir)


def get_apk_info(testing_result_dir: str, app_name: str):
    base_name = os.path.basename(testing_result_dir)
    target_apk_file_name = str(base_name.split(".apk")[0]) + ".apk"

    target_apk_file_path = os.path.join("../" + app_name, target_apk_file_name)
    get_app_package_name_cmd = "aapt dump badging " + target_apk_file_path + " | grep package | awk '{print $2}' | sed s/name=//g | sed s/\\'//g"
    app_package_name = ""

    try:
        p = subprocess.Popen(get_app_package_name_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # clear the output
        app_package_name = p.communicate()[0].decode('utf-8').strip()
        print(app_package_name)
    except os.error as e:
        print(e)

    return target_apk_file_name, app_package_name


def main(args: Namespace):
    # collect all testing result dirs
    all_testing_results_dirs = []
    subdirs = os.listdir(args.o)
    for subdir in subdirs:
        # print(subdir)
        subdir_path = os.path.join(args.o, subdir)
        if os.path.isdir(subdir_path):
            all_testing_results_dirs.append(subdir_path)

    # print(all_testing_results_dirs)
    # the dict only used for collecting non-target crashes
    #   key: the apk file name
    #   value: list of signatures of crash stacks
    other_crashes_signature_str_dict: Dict[str, List[str]] = {}
    other_crashes_complete_exception_trace_dict: Dict[str, List[List[str]]] = {}

    # check crash
    for app_name in app_crash_data:

        if args.app_name is not None and args.app_name != app_name:
            # skip unrelated apps if args.app_name is given
            continue

        # if args.monkey and app_name == "ActivityDiary":
        #    # TODO special check for Monkey's ActivityDiary [should be removed in the future]
        #    continue

        print(args.app_name)

        issue_crash_data = app_crash_data[app_name]

        for issue_id in issue_crash_data:

            if args.issue_id is not None and args.issue_id != issue_id:
                # skip unrelated issues if args.issue_id is given
                continue

            issue_testing_result_dirs = get_testing_result_dir(all_testing_results_dirs,
                                                               app_name,
                                                               issue_id)

            if len(issue_testing_result_dirs) == 0:
                continue

            log_tag_name = '[' + app_name + ', ' + issue_id + '] '

            print("\n\n=========")

            crash_signature_strs = issue_crash_data[issue_id]

            # scanning the testing results of the given issue
            for result_dir in issue_testing_result_dirs:

                logcat_file_path = ""
                testing_time_file_path = ""
                login_file_path = ""

                if args.monkey:
                    # Monkey
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "monkey_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.ape:
                    # Ape
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "ape_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.combo:
                    # ComboDroid
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "combo_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H-%M-%S'

                if args.timemachine:
                    # TimeMachine
                    logcat_file_path = os.path.join(result_dir, "timemachine-output/crashes.log")
                    login_file_path = os.path.join(result_dir, "timemachine-run.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "timemachine-output/run_time.log")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.humanoid:
                    # Humanoid
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "humandroid_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.droidbot:
                    # Droidbot
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "droidbot_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.sapienz:
                    # Sapienz
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "sapienz_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.qtesting:
                    # Q-testing
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "qtesting_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.weighted:
                    # Q-testing
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "weighted_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if args.fastbot:
                    # Fastbot
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "fastbot_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'
                    
                if args.wetest:
                    # WeTest
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "wetest_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'
                
                if args.fastbot_new:
                    # Fastbot
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "fastbot_new_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'
                    
                if args.wetest_new:
                    # WeTest
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "wetest_new_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'
                
                if args.newmonkey:
                    # Newmonkey
                    logcat_file_path = os.path.join(result_dir, "logcat.log")
                    login_file_path = os.path.join(result_dir, "login.log")
                    testing_time_file_path = os.path.join(result_dir,
                                                          "newmonkey_testing_time_on_emulator.txt")
                    testing_time_datetime_str = '%Y-%m-%d-%H:%M:%S'

                if os.path.exists(logcat_file_path) and os.path.exists(testing_time_file_path):

                    print('\n')
                    print(log_tag_name + 'scanning (%s) ' % os.path.basename(result_dir))

                    testing_time_file = open(testing_time_file_path, 'r')
                    lines = testing_time_file.readlines()
                    for line in lines:
                        print(log_tag_name + 'testing time: %s ' % line.strip())
                    if len(lines) == 0:
                        # double check on the file content on the testing time
                        print(log_tag_name + 'this run does not have recorded testing time, skip this run!')
                        continue

                    time.sleep(1)

                    # get the start testing datetime
                    if args.timemachine:
                        # special handle timemachine
                        start_testing_datetime_str = lines[0][0:19]
                    else:
                        start_testing_datetime_str = lines[0].strip()
                    print("the start testing time is: %s" % start_testing_datetime_str)
                    start_testing_datetime_obj = datetime.datetime.strptime(start_testing_datetime_str,
                                                                            testing_time_datetime_str)
                    print("the start testing time (parsed) is: %s" % start_testing_datetime_obj)

                    if os.path.exists(login_file_path):
                        cmd = 'grep ' + "\"" + "Login SUCCESS" + "\" " + login_file_path
                        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        # clear the output
                        output = p.communicate()[0].decode('utf-8').strip()
                        if len(output) != 0:
                            print(log_tag_name + "Login SUCCESS")
                        else:
                            print(log_tag_name + "Login FAIL?")

                    # split the logcat file into separate stack traces
                    crash_stack_traces: Dict[str, List[str]] = {}
                    logcat_file = open(logcat_file_path, 'r')

                    if args.timemachine:

                        if not args.other_crashes:
                            # special handle for TimeMachine (for target crash)
                            cache_list = []
                            for line in logcat_file.readlines():
                                if line.startswith("---"):
                                    continue

                                if line.startswith("["):
                                    time_label = line.strip()
                                    crash_stack_traces[time_label] = cache_list
                                    cache_list = []
                                else:
                                    cache_list.append(line)
                        else:
                            # special handle for TimeMachine (for non-target crash)
                            fake_time_label_index = 1
                            fake_time_label = "fake_time_"
                            for line in logcat_file.readlines():
                                if line.startswith("---") or line.startswith("["):
                                    fake_time_label_index += 1
                                    fake_time_label = fake_time_label + str(fake_time_label_index)
                                    continue

                                if fake_time_label not in crash_stack_traces:
                                    crash_stack_traces[fake_time_label] = [line]
                                else:
                                    crash_stack_traces[fake_time_label].append(line)

                    else:
                        for line in logcat_file.readlines():
                            if line.startswith("---"):
                                continue

                            res = [i for i in range(len(line)) if line.startswith(':', i)]
                            try:
                                # hot fix
                                time_label = line[0:res[2]]  # the third ":" is the split point
                            except IndexError:
                                print("Catch IndexError when paring logcat!")
                                continue
                            if time_label not in crash_stack_traces:
                                crash_stack_traces[time_label] = [line]
                            else:
                                crash_stack_traces[time_label].append(line)
                    logcat_file.close()

                    if args.other_crashes:

                        # check the number of other crashes that were detected by-product
                        app_dir_name = get_app_name(result_dir)
                        apk_file_name, app_package_name = get_apk_info(result_dir, app_dir_name)

                        print("apk file name: %s" % apk_file_name)
                        print("apk package name: %s" % app_package_name)

                        if app_package_name.endswith(".debug") or app_package_name.endswith(".debug.ting"):
                            app_package_name = app_package_name.split(".debug")[0]
                        if app_package_name.endswith(".client"):
                            app_package_name = "com.owncloud.android"
                        if app_package_name.endswith(".activity"):
                            app_package_name = app_package_name.split(".activity")[0]
                        if app_package_name.endswith(".quicknote"):
                            app_package_name = "com.maubis.scarlet"
                        if app_package_name.endswith(".attendee"):
                            app_package_name = "org.fossasia.openevent"

                        for time_label in crash_stack_traces:

                            if args.timemachine:
                                # Special handling on timemachine

                                target_stack = crash_stack_traces[time_label]

                                # split the target_stack into sub exception traces
                                sub_exception_stacks: Dict[str, List[str]] = {}
                                for line in target_stack:
                                    res = [i for i in range(len(line)) if line.startswith(':', i)]
                                    print(line)
                                    if len(res) < 3:
                                        # special handling for the case like
                                        #   "AndroidRuntime: 	at android.os.BinderProxy.transactNative(Native Method)"
                                        continue
                                    else:
                                        local_time_label = line[0:res[2]]  # the third ":" is the split point
                                    if local_time_label not in sub_exception_stacks:
                                        sub_exception_stacks[local_time_label] = [line]
                                    else:
                                        sub_exception_stacks[local_time_label].append(line)

                                for local_time_label in sub_exception_stacks:
                                    if "AndroidRuntime" in local_time_label or "ACRA" in local_time_label \
                                            or "CustomActivityOnCrash" in local_time_label \
                                            or "CrashAnrDetector" in local_time_label:
                                        # focus on "AndroidRuntime" bugs
                                        pass
                                    else:
                                        continue

                                    uniqe_signature_of_crash_stack = ""

                                    sub_exception_stack = sub_exception_stacks[local_time_label]
                                    for line in sub_exception_stack:
                                        if "at " in line and app_package_name in line:
                                            line_without_time_label = line.replace(local_time_label + ":", "").strip()
                                            uniqe_signature_of_crash_stack += line_without_time_label

                                    if uniqe_signature_of_crash_stack == "":
                                        continue

                                    print("\n-- signature --")
                                    print(uniqe_signature_of_crash_stack)
                                    print("----")

                                    if apk_file_name not in other_crashes_signature_str_dict:
                                        other_crashes_signature_str_dict[apk_file_name] = [
                                            uniqe_signature_of_crash_stack]
                                        other_crashes_complete_exception_trace_dict[apk_file_name] = [
                                            sub_exception_stack]
                                    else:
                                        if uniqe_signature_of_crash_stack not in other_crashes_signature_str_dict[
                                            apk_file_name]:
                                            # check existence
                                            other_crashes_signature_str_dict[apk_file_name].append(
                                                uniqe_signature_of_crash_stack)
                                            other_crashes_complete_exception_trace_dict[apk_file_name].append(
                                                sub_exception_stack)

                            else:

                                target_stack = crash_stack_traces[time_label]
                                uniqe_signature_of_crash_stack = ""

                                if "AndroidRuntime" in time_label or "ACRA" in time_label \
                                        or "CustomActivityOnCrash" in time_label \
                                        or "CrashAnrDetector" in time_label:
                                    # focus on "AndroidRuntime" bugs
                                    pass
                                else:
                                    continue

                                for line in target_stack:

                                    if "at " in line and app_package_name in line:
                                        line_without_time_label = line.replace(time_label + ":", "").strip()
                                        uniqe_signature_of_crash_stack += line_without_time_label

                                if uniqe_signature_of_crash_stack == "":
                                    continue

                                print("\n-- signature --")
                                print(uniqe_signature_of_crash_stack)
                                print("----")

                                if apk_file_name not in other_crashes_signature_str_dict:
                                    other_crashes_signature_str_dict[apk_file_name] = [uniqe_signature_of_crash_stack]
                                    other_crashes_complete_exception_trace_dict[apk_file_name] = [target_stack]
                                else:
                                    if uniqe_signature_of_crash_stack not in other_crashes_signature_str_dict[
                                        apk_file_name]:
                                        # check existence
                                        other_crashes_signature_str_dict[apk_file_name].append(
                                            uniqe_signature_of_crash_stack)
                                        other_crashes_complete_exception_trace_dict[apk_file_name].append(target_stack)

                            # print("--")
                            # print(len(set(other_crashes_dict[app_name])))
                            # print(other_crashes_dict[app_name])
                            # print("--")

                        if apk_file_name in other_crashes_signature_str_dict:
                            number_of_unique_other_crashes = len(set(other_crashes_signature_str_dict[apk_file_name]))
                            print("#unique other crashes: %d" % number_of_unique_other_crashes)
                        else:
                            number_of_unique_other_crashes = 0

                        # output to final result file
                        if args.final_result_csv_file_path is not None:
                            with open(args.final_result_csv_file_path, "a") as csv_file:
                                writer = csv.writer(csv_file)
                                writer.writerow([apk_file_name, issue_id, os.path.basename(result_dir),
                                                 number_of_unique_other_crashes])
                            csv_file.close()

                    else:
                        # check the existence of target crashes (i.e., the critical crash we concern)
                        number_of_matched_crash = 0
                        crash_triggering_time_durations = []
                        for time_label in crash_stack_traces:
                            target_stack = crash_stack_traces[time_label]

                            is_matched = True
                            for signature_str in crash_signature_strs:

                                exist = False
                                for line in target_stack:
                                    if signature_str in line:
                                        exist = True
                                        break
                                if exist:
                                    continue
                                else:
                                    is_matched = False
                                    break

                            if is_matched:

                                # compute the time duration to trigger the crash
                                if args.timemachine:
                                    # print("time label: %s" % time_label)
                                    matched_datetime_str = time_label.replace("[", "").replace("]", "")
                                    crash_triggering_datetime_obj = datetime.datetime.strptime(matched_datetime_str,
                                                                                               '%Y-%m-%d-%H:%M:%S')
                                else:
                                    matched_datetime_str = "{}-{}".format(start_testing_datetime_obj.year, time_label.split('.')[0])
                                    crash_triggering_datetime_obj = datetime.datetime.strptime(matched_datetime_str,
                                                                                               '%Y-%m-%d %H:%M:%S')

                                tmp_time_duration_in_minutes = (
                                                                       crash_triggering_datetime_obj - start_testing_datetime_obj).total_seconds() / 60
                                crash_triggering_time_durations.append("{:.0f}".format(tmp_time_duration_in_minutes))

                                number_of_matched_crash += 1

                        if number_of_matched_crash > 0:
                            print(log_tag_name + "the crash was triggered (%d) times" % number_of_matched_crash)
                            print(log_tag_name + "the time duration: %s (mins)" % crash_triggering_time_durations)
                            # if args.v:
                            #     print('---')
                            #     # verbose mode
                            #     print(output)
                            #     print('---')

                        # output to final result file
                        if args.final_result_csv_file_path is not None:

                            if not args.simple_format:
                                with open(args.final_result_csv_file_path, "a") as csv_file:
                                    writer = csv.writer(csv_file)
                                    writer.writerow([app_name, issue_id, os.path.basename(result_dir),
                                                     len(crash_triggering_time_durations)])
                                    for time_duration in crash_triggering_time_durations:
                                        writer.writerow(["", "", "", time_duration])
                                csv_file.close()
                            else:

                                if len(crash_triggering_time_durations) > 0:
                                    # output in a simple format: only output triggered bugs and its first triggering time
                                    with open(args.final_result_csv_file_path, "a") as csv_file:
                                        writer = csv.writer(csv_file)
                                        writer.writerow([app_name, issue_id, os.path.basename(result_dir),
                                                         len(crash_triggering_time_durations),
                                                         crash_triggering_time_durations[0]])
                                    csv_file.close()

                else:
                    print('\n')
                    print(log_tag_name + 'scanning (%s) ' % os.path.basename(result_dir))
                    print(log_tag_name + "Warning: logcat file or testing time file in (%s) does not exist!" %
                          os.path.basename(result_dir))
                    continue

    if args.other_crashes:

        total_number_of_other_crashes = 0
        for apk_file_name in other_crashes_signature_str_dict:
            print("%s: %d" % (apk_file_name, len(set(other_crashes_signature_str_dict[apk_file_name]))))
            total_number_of_other_crashes += len(set(other_crashes_signature_str_dict[apk_file_name]))

        print("#total other crashes: %d" % total_number_of_other_crashes)

        # output the complete stack traces of all the other crashes (i.e., non-target crashes)
        tmp_output_dir = os.path.join(args.o, "other_crashes")
        if os.path.exists(tmp_output_dir):
            shutil.rmtree(tmp_output_dir)

        for apk_file_name in other_crashes_complete_exception_trace_dict:
            print("dump complete crash stack for: %s" % apk_file_name)
            tmp_output_dir_of_each_apk = os.path.join(tmp_output_dir, apk_file_name)
            if not os.path.exists(tmp_output_dir_of_each_apk):
                os.makedirs(tmp_output_dir_of_each_apk)
            stack_traces: List[List[str]] = other_crashes_complete_exception_trace_dict[apk_file_name]
            file_index = 0
            for stack_trace in stack_traces:
                tmp_file_path = os.path.join(tmp_output_dir_of_each_apk, "crash_stack_" + str(file_index) + ".txt")
                file_index += 1
                with open(tmp_file_path, "w") as tmp_file:
                    for line in stack_trace:
                        tmp_file.write(line)
                tmp_file.close()


if __name__ == '__main__':

    ap = ArgumentParser()

    ap.add_argument('-o', required=True, help="the output directory of testing results")
    ap.add_argument('-v', default=False, action='store_true')

    # supported fuzzing tools
    ap.add_argument('--monkey', default=False, action='store_true')
    ap.add_argument('--ape', default=False, action='store_true')
    ap.add_argument('--timemachine', default=False, action='store_true')
    ap.add_argument('--combo', default=False, action='store_true')
    ap.add_argument('--humanoid', default=False, action='store_true')
    ap.add_argument('--sapienz', default=False, action='store_true')
    ap.add_argument('--qtesting', default=False, action='store_true')
    ap.add_argument('--weighted', default=False, action='store_true')
    ap.add_argument('--fastbot', default=False, action='store_true')
    ap.add_argument('--wetest', default=False, action='store_true')
    ap.add_argument('--fastbot_new', default=False, action='store_true')
    ap.add_argument('--wetest_new', default=False, action='store_true')
    ap.add_argument('--newmonkey', default=False, action='store_true')
    ap.add_argument('--droidbot', default=False, action='store_true')
                                                                                                           
    ap.add_argument('--app', type=str, dest='app_name')
    ap.add_argument('--id', type=str, dest='issue_id')
    ap.add_argument('--csv', type=str, dest='final_result_csv_file_path')
    ap.add_argument('--simple', default=False, action='store_true', dest='simple_format',
                    help="standard output in a simple format")
    ap.add_argument('--other_crashes', default=False, action='store_true', dest='other_crashes')
                             
    args = ap.parse_args()
                  
    if not os.path.exists(args.o):
        ap.error("Error: the output directory does not exist!")

    if args.final_result_csv_file_path is not None and os.path.exists(args.final_result_csv_file_path):
        os.remove(args.final_result_csv_file_path)

    main(args)
