#!/usr/bin/env python
# -*- coding: utf-8 -*-

# THIS FILE WAS GENERATED BY generate_classes.py - DO NOT EDIT #
# (Generated on 2019-09-11 13:41:33.777292) #

from .base_classes import BaseEvent


class Heartbeat(BaseEvent):
    """
    Emitted every 2 seconds after enabling it by calling SetHeartbeat.

    :Returns:
       *pulse*
            type: boolean
            Toggles between every JSON message as an "I am alive" indicator.
       *current_profile*
            type: string (optional)
            Current active profile.
       *current_scene*
            type: string (optional)
            Current active scene.
       *streaming*
            type: boolean (optional)
            Current streaming state.
       *total_stream_time*
            type: int (optional)
            Total time (in seconds) since the stream started.
       *total_stream_bytes*
            type: int (optional)
            Total bytes sent since the stream started.
       *total_stream_frames*
            type: int (optional)
            Total frames streamed since the stream started.
       *recording*
            type: boolean (optional)
            Current recording state.
       *total_record_time*
            type: int (optional)
            Total time (in seconds) since recording started.
       *total_record_bytes*
            type: int (optional)
            Total bytes recorded since the recording started.
       *total_record_frames*
            type: int (optional)
            Total frames recorded since the recording started.
       *stats*
            type: OBSStats
            OBS Stats
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'Heartbeat'
        self._returns['pulse'] = None
        self._returns['current-profile'] = None
        self._returns['current-scene'] = None
        self._returns['streaming'] = None
        self._returns['total-stream-time'] = None
        self._returns['total-stream-bytes'] = None
        self._returns['total-stream-frames'] = None
        self._returns['recording'] = None
        self._returns['total-record-time'] = None
        self._returns['total-record-bytes'] = None
        self._returns['total-record-frames'] = None
        self._returns['stats'] = None

    @property
    def pulse(self):
        return self._returns['pulse']

    @property
    def current_profile(self):
        return self._returns['current-profile']

    @property
    def current_scene(self):
        return self._returns['current-scene']

    @property
    def streaming(self):
        return self._returns['streaming']

    @property
    def total_stream_time(self):
        return self._returns['total-stream-time']

    @property
    def total_stream_bytes(self):
        return self._returns['total-stream-bytes']

    @property
    def total_stream_frames(self):
        return self._returns['total-stream-frames']

    @property
    def recording(self):
        return self._returns['recording']

    @property
    def total_record_time(self):
        return self._returns['total-record-time']

    @property
    def total_record_bytes(self):
        return self._returns['total-record-bytes']

    @property
    def total_record_frames(self):
        return self._returns['total-record-frames']

    @property
    def stats(self):
        return self._returns['stats']


class BroadcastCustomMessage(BaseEvent):
    """
    A custom broadcast message was received

    :Returns:
       *realm*
            type: String
            Identifier provided by the sender
       *data*
            type: Object
            User-defined data
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'BroadcastCustomMessage'
        self._returns['realm'] = None
        self._returns['data'] = None

    @property
    def realm(self):
        return self._returns['realm']

    @property
    def data(self):
        return self._returns['data']


class Exiting(BaseEvent):
    """
    OBS is exiting.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'Exiting'


class ProfileChanged(BaseEvent):
    """
    Triggered when switching to another profile or when renaming the current profile.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'ProfileChanged'


class ProfileListChanged(BaseEvent):
    """
    Triggered when a profile is created, added, renamed, or removed.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'ProfileListChanged'


class RecordingStarting(BaseEvent):
    """
    A request to start recording has been issued.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'RecordingStarting'


class RecordingStarted(BaseEvent):
    """
    Recording started successfully.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'RecordingStarted'


class RecordingStopping(BaseEvent):
    """
    A request to stop recording has been issued.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'RecordingStopping'


class RecordingStopped(BaseEvent):
    """
    Recording stopped successfully.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'RecordingStopped'


class RecordingPaused(BaseEvent):
    """
    Current recording paused
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'RecordingPaused'


class RecordingResumed(BaseEvent):
    """
    Current recording resumed
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'RecordingResumed'


class ReplayStarting(BaseEvent):
    """
    A request to start the replay buffer has been issued.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'ReplayStarting'


class ReplayStarted(BaseEvent):
    """
    Replay Buffer started successfully
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'ReplayStarted'


class ReplayStopping(BaseEvent):
    """
    A request to stop the replay buffer has been issued.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'ReplayStopping'


class ReplayStopped(BaseEvent):
    """
    Replay Buffer stopped successfully
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'ReplayStopped'


class SwitchScenes(BaseEvent):
    """
    Indicates a scene change.

    :Returns:
       *scene_name*
            type: String
            The new scene.
       *sources*
            type: Array<SceneItem>
            List of scene items in the new scene. Same specification as [`GetCurrentScene`](#getcurrentscene).
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SwitchScenes'
        self._returns['scene-name'] = None
        self._returns['sources'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def sources(self):
        return self._returns['sources']


class ScenesChanged(BaseEvent):
    """
    The scene list has been modified.
    Scenes have been added, removed, or renamed.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'ScenesChanged'


class SceneCollectionChanged(BaseEvent):
    """
    Triggered when switching to another scene collection or when renaming the current scene collection.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneCollectionChanged'


class SceneCollectionListChanged(BaseEvent):
    """
    Triggered when a scene collection is created, added, renamed, or removed.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneCollectionListChanged'


class SourceCreated(BaseEvent):
    """
    A source has been created. A source can be an input, a scene or a transition.

    :Returns:
       *source_name*
            type: String
            Source name
       *source_type*
            type: String
            Source type. Can be "input", "scene", "transition" or "filter".
       *source_kind*
            type: String
            Source kind.
       *source_settings*
            type: Object
            Source settings
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceCreated'
        self._returns['sourceName'] = None
        self._returns['sourceType'] = None
        self._returns['sourceKind'] = None
        self._returns['sourceSettings'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def source_type(self):
        return self._returns['sourceType']

    @property
    def source_kind(self):
        return self._returns['sourceKind']

    @property
    def source_settings(self):
        return self._returns['sourceSettings']


class SourceDestroyed(BaseEvent):
    """
    A source has been destroyed/removed. A source can be an input, a scene or a transition.

    :Returns:
       *source_name*
            type: String
            Source name
       *source_type*
            type: String
            Source type. Can be "input", "scene", "transition" or "filter".
       *source_kind*
            type: String
            Source kind.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceDestroyed'
        self._returns['sourceName'] = None
        self._returns['sourceType'] = None
        self._returns['sourceKind'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def source_type(self):
        return self._returns['sourceType']

    @property
    def source_kind(self):
        return self._returns['sourceKind']


class SourceVolumeChanged(BaseEvent):
    """
    The volume of a source has changed.

    :Returns:
       *source_name*
            type: String
            Source name
       *volume*
            type: float
            Source volume
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceVolumeChanged'
        self._returns['sourceName'] = None
        self._returns['volume'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def volume(self):
        return self._returns['volume']


class SourceMuteStateChanged(BaseEvent):
    """
    A source has been muted or unmuted.

    :Returns:
       *source_name*
            type: String
            Source name
       *muted*
            type: boolean
            Mute status of the source
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceMuteStateChanged'
        self._returns['sourceName'] = None
        self._returns['muted'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def muted(self):
        return self._returns['muted']


class SourceAudioSyncOffsetChanged(BaseEvent):
    """
    The audio sync offset of a source has changed.

    :Returns:
       *source_name*
            type: String
            Source name
       *sync_offset*
            type: int
            Audio sync offset of the source (in nanoseconds)
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceAudioSyncOffsetChanged'
        self._returns['sourceName'] = None
        self._returns['syncOffset'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def sync_offset(self):
        return self._returns['syncOffset']


class SourceAudioMixersChanged(BaseEvent):
    """
    Audio mixer routing changed on a source.

    :Returns:
       *source_name*
            type: String
            Source name
       *mixers*
            type: Array<Object>
            Routing status of the source for each audio mixer (array of 6 values)
       *mixers.*.id*
            type: int
            Mixer number
       *mixers.*.enabled*
            type: boolean
            Routing status
       *hex_mixers_value*
            type: String
            Raw mixer flags (little-endian, one bit per mixer) as an hexadecimal value
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceAudioMixersChanged'
        self._returns['sourceName'] = None
        self._returns['mixers'] = None
        self._returns['hexMixersValue'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def mixers(self):
        return self._returns['mixers']

    @property
    def hex_mixers_value(self):
        return self._returns['hexMixersValue']


class SourceRenamed(BaseEvent):
    """
    A source has been renamed.

    :Returns:
       *previous_name*
            type: String
            Previous source name
       *new_name*
            type: String
            New source name
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceRenamed'
        self._returns['previousName'] = None
        self._returns['newName'] = None

    @property
    def previous_name(self):
        return self._returns['previousName']

    @property
    def new_name(self):
        return self._returns['newName']


class SourceFilterAdded(BaseEvent):
    """
    A filter was added to a source.

    :Returns:
       *source_name*
            type: String
            Source name
       *filter_name*
            type: String
            Filter name
       *filter_type*
            type: String
            Filter type
       *filter_settings*
            type: Object
            Filter settings
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceFilterAdded'
        self._returns['sourceName'] = None
        self._returns['filterName'] = None
        self._returns['filterType'] = None
        self._returns['filterSettings'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def filter_name(self):
        return self._returns['filterName']

    @property
    def filter_type(self):
        return self._returns['filterType']

    @property
    def filter_settings(self):
        return self._returns['filterSettings']


class SourceFilterRemoved(BaseEvent):
    """
    A filter was removed from a source.

    :Returns:
       *source_name*
            type: String
            Source name
       *filter_name*
            type: String
            Filter name
       *filter_type*
            type: String
            Filter type
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceFilterRemoved'
        self._returns['sourceName'] = None
        self._returns['filterName'] = None
        self._returns['filterType'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def filter_name(self):
        return self._returns['filterName']

    @property
    def filter_type(self):
        return self._returns['filterType']


class SourceFiltersReordered(BaseEvent):
    """
    Filters in a source have been reordered.

    :Returns:
       *source_name*
            type: String
            Source name
       *filters*
            type: Array<Object>
            Ordered Filters list
       *filters.*.name*
            type: String
            Filter name
       *filters.*.type*
            type: String
            Filter type
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceFiltersReordered'
        self._returns['sourceName'] = None
        self._returns['filters'] = None

    @property
    def source_name(self):
        return self._returns['sourceName']

    @property
    def filters(self):
        return self._returns['filters']


class SourceOrderChanged(BaseEvent):
    """
    Scene items have been reordered.

    :Returns:
       *scene_name*
            type: String
            Name of the scene where items have been reordered.
       *scene_items*
            type: Array<Object>
            Ordered list of scene items
       *scene_items.*.source_name*
            type: String
            Item source name
       *scene_items.*.item_id*
            type: int
            Scene item unique ID
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SourceOrderChanged'
        self._returns['scene-name'] = None
        self._returns['scene-items'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def scene_items(self):
        return self._returns['scene-items']


class SceneItemAdded(BaseEvent):
    """
    An item has been added to the current scene.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item added to the scene.
       *item_id*
            type: int
            Scene item ID
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneItemAdded'
        self._returns['scene-name'] = None
        self._returns['item-name'] = None
        self._returns['item-id'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def item_name(self):
        return self._returns['item-name']

    @property
    def item_id(self):
        return self._returns['item-id']


class SceneItemRemoved(BaseEvent):
    """
    An item has been removed from the current scene.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item removed from the scene.
       *item_id*
            type: int
            Scene item ID
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneItemRemoved'
        self._returns['scene-name'] = None
        self._returns['item-name'] = None
        self._returns['item-id'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def item_name(self):
        return self._returns['item-name']

    @property
    def item_id(self):
        return self._returns['item-id']


class SceneItemVisibilityChanged(BaseEvent):
    """
    An item's visibility has been toggled.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *item_visible*
            type: boolean
            New visibility state of the item.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneItemVisibilityChanged'
        self._returns['scene-name'] = None
        self._returns['item-name'] = None
        self._returns['item-id'] = None
        self._returns['item-visible'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def item_name(self):
        return self._returns['item-name']

    @property
    def item_id(self):
        return self._returns['item-id']

    @property
    def item_visible(self):
        return self._returns['item-visible']


class SceneItemTransformChanged(BaseEvent):
    """
    An item's transform has been changed.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *transform*
            type: SceneItemTransform
            Scene item transform properties
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneItemTransformChanged'
        self._returns['scene-name'] = None
        self._returns['item-name'] = None
        self._returns['item-id'] = None
        self._returns['transform'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def item_name(self):
        return self._returns['item-name']

    @property
    def item_id(self):
        return self._returns['item-id']

    @property
    def transform(self):
        return self._returns['transform']


class SceneItemSelected(BaseEvent):
    """
    A scene item is selected.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Name of the item in the scene.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneItemSelected'
        self._returns['scene-name'] = None
        self._returns['item-name'] = None
        self._returns['item-id'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def item_name(self):
        return self._returns['item-name']

    @property
    def item_id(self):
        return self._returns['item-id']


class SceneItemDeselected(BaseEvent):
    """
    A scene item is deselected.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Name of the item in the scene.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SceneItemDeselected'
        self._returns['scene-name'] = None
        self._returns['item-name'] = None
        self._returns['item-id'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def item_name(self):
        return self._returns['item-name']

    @property
    def item_id(self):
        return self._returns['item-id']


class StreamStarting(BaseEvent):
    """
    A request to start streaming has been issued.

    :Returns:
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'StreamStarting'
        self._returns['preview-only'] = None

    @property
    def preview_only(self):
        return self._returns['preview-only']


class StreamStarted(BaseEvent):
    """
    Streaming started successfully.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'StreamStarted'


class StreamStopping(BaseEvent):
    """
    A request to stop streaming has been issued.

    :Returns:
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'StreamStopping'
        self._returns['preview-only'] = None

    @property
    def preview_only(self):
        return self._returns['preview-only']


class StreamStopped(BaseEvent):
    """
    Streaming stopped successfully.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'StreamStopped'


class StreamStatus(BaseEvent):
    """
    Emit every 2 seconds.

    :Returns:
       *streaming*
            type: boolean
            Current streaming state.
       *recording*
            type: boolean
            Current recording state.
       *replay_buffer_active*
            type: boolean
            Replay Buffer status
       *bytes_per_sec*
            type: int
            Amount of data per second (in bytes) transmitted by the stream encoder.
       *kbits_per_sec*
            type: int
            Amount of data per second (in kilobits) transmitted by the stream encoder.
       *strain*
            type: double
            Percentage of dropped frames.
       *total_stream_time*
            type: int
            Total time (in seconds) since the stream started.
       *num_total_frames*
            type: int
            Total number of frames transmitted since the stream started.
       *num_dropped_frames*
            type: int
            Number of frames dropped by the encoder since the stream started.
       *fps*
            type: double
            Current framerate.
       *render_total_frames*
            type: int
            Number of frames rendered
       *render_missed_frames*
            type: int
            Number of frames missed due to rendering lag
       *output_total_frames*
            type: int
            Number of frames outputted
       *output_skipped_frames*
            type: int
            Number of frames skipped due to encoding lag
       *average_frame_time*
            type: double
            Average frame time (in milliseconds)
       *cpu_usage*
            type: double
            Current CPU usage (percentage)
       *memory_usage*
            type: double
            Current RAM usage (in megabytes)
       *free_disk_space*
            type: double
            Free recording disk space (in megabytes)
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'StreamStatus'
        self._returns['streaming'] = None
        self._returns['recording'] = None
        self._returns['replay-buffer-active'] = None
        self._returns['bytes-per-sec'] = None
        self._returns['kbits-per-sec'] = None
        self._returns['strain'] = None
        self._returns['total-stream-time'] = None
        self._returns['num-total-frames'] = None
        self._returns['num-dropped-frames'] = None
        self._returns['fps'] = None
        self._returns['render-total-frames'] = None
        self._returns['render-missed-frames'] = None
        self._returns['output-total-frames'] = None
        self._returns['output-skipped-frames'] = None
        self._returns['average-frame-time'] = None
        self._returns['cpu-usage'] = None
        self._returns['memory-usage'] = None
        self._returns['free-disk-space'] = None
        self._returns['preview-only'] = None

    @property
    def streaming(self):
        return self._returns['streaming']

    @property
    def recording(self):
        return self._returns['recording']

    @property
    def replay_buffer_active(self):
        return self._returns['replay-buffer-active']

    @property
    def bytes_per_sec(self):
        return self._returns['bytes-per-sec']

    @property
    def kbits_per_sec(self):
        return self._returns['kbits-per-sec']

    @property
    def strain(self):
        return self._returns['strain']

    @property
    def total_stream_time(self):
        return self._returns['total-stream-time']

    @property
    def num_total_frames(self):
        return self._returns['num-total-frames']

    @property
    def num_dropped_frames(self):
        return self._returns['num-dropped-frames']

    @property
    def fps(self):
        return self._returns['fps']

    @property
    def render_total_frames(self):
        return self._returns['render-total-frames']

    @property
    def render_missed_frames(self):
        return self._returns['render-missed-frames']

    @property
    def output_total_frames(self):
        return self._returns['output-total-frames']

    @property
    def output_skipped_frames(self):
        return self._returns['output-skipped-frames']

    @property
    def average_frame_time(self):
        return self._returns['average-frame-time']

    @property
    def cpu_usage(self):
        return self._returns['cpu-usage']

    @property
    def memory_usage(self):
        return self._returns['memory-usage']

    @property
    def free_disk_space(self):
        return self._returns['free-disk-space']

    @property
    def preview_only(self):
        return self._returns['preview-only']


class PreviewSceneChanged(BaseEvent):
    """
    The selected preview scene has changed (only available in Studio Mode).

    :Returns:
       *scene_name*
            type: String
            Name of the scene being previewed.
       *sources*
            type: Array<SceneItem>
            List of sources composing the scene. Same specification as [`GetCurrentScene`](#getcurrentscene).
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'PreviewSceneChanged'
        self._returns['scene-name'] = None
        self._returns['sources'] = None

    @property
    def scene_name(self):
        return self._returns['scene-name']

    @property
    def sources(self):
        return self._returns['sources']


class StudioModeSwitched(BaseEvent):
    """
    Studio Mode has been enabled or disabled.

    :Returns:
       *new_state*
            type: boolean
            The new enabled state of Studio Mode.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'StudioModeSwitched'
        self._returns['new-state'] = None

    @property
    def new_state(self):
        return self._returns['new-state']


class SwitchTransition(BaseEvent):
    """
    The active transition has been changed.

    :Returns:
       *transition_name*
            type: String
            The name of the new active transition.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'SwitchTransition'
        self._returns['transition-name'] = None

    @property
    def transition_name(self):
        return self._returns['transition-name']


class TransitionListChanged(BaseEvent):
    """
    The list of available transitions has been modified.
    Transitions have been added, removed, or renamed.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'TransitionListChanged'


class TransitionDurationChanged(BaseEvent):
    """
    The active transition duration has been changed.

    :Returns:
       *new_duration*
            type: int
            New transition duration.
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'TransitionDurationChanged'
        self._returns['new-duration'] = None

    @property
    def new_duration(self):
        return self._returns['new-duration']


class TransitionBegin(BaseEvent):
    """
    A transition (other than "cut") has begun.

    :Returns:
       *name*
            type: String
            Transition name.
       *duration*
            type: int
            Transition duration (in milliseconds).
       *from_scene*
            type: String
            Source scene of the transition
       *to_scene*
            type: String
            Destination scene of the transition
    """
    def __init__(self):
        BaseEvent.__init__(self)
        self._name = 'TransitionBegin'
        self._returns['name'] = None
        self._returns['duration'] = None
        self._returns['from-scene'] = None
        self._returns['to-scene'] = None

    @property
    def name(self):
        return self._returns['name']

    @property
    def duration(self):
        return self._returns['duration']

    @property
    def from_scene(self):
        return self._returns['from-scene']

    @property
    def to_scene(self):
        return self._returns['to-scene']

