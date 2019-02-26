from information_retrieval import extraction as ir
from message import messenger as mes
import argparse
import librosa
from typing import List, Dict, Any
from filter import vamp as vamp_filter
from convert import vamp as vamp_convert
from preprocess import vamp as prep_vamp
from postprocess import music_xml as postp_mxl
from music import song
import music21
import json
from utils import utils

# s = music21.stream.Stream()
# s.insert(0, music21.note.Note('C4', quarterLength=4))
# s.repeatInsert(music21.note.Note('b-4', quarterLength=0.5), [x * 0.5 for x in list(range(8))])
# s.makeVoices(inPlace=True)
# s.show()


# len(s.voices)
#
# [n.pitch for n in s.voices[0].notes]
#
# [str(n.pitch) for n in s.voices[1].notes]

# exit(0)

# note1 = music21.note.Note('C')
#
# note3 = music21.note.Note('E')
#
# # note1.offset = 2.0
#
# note1.duration = music21.duration.Duration(1.0)
#
# note3.duration = music21.duration.Duration(1.0)
#
# note2 = music21.note.Note('D')
#
# note4 = music21.note.Note('F')
#
# # note2.offset = 4.0
#
# note2.duration = music21.duration.Duration(1.0)
#
# note4.duration = music21.duration.Duration(1.0)
#
# score = music21.stream.Part()
#
# score.insert(2.0, note1)
#
# score.insert(2.0, note3)
#
# score.insert(5.0, note2)
#
# score.insert(5.0, note4)
#
# score.show()
#
# # score.makeRests(fillGaps=True, inPlace=False).makeMeasures(inPlace=False).show()
#
# exit(0)

def main(args):
    messenger = mes.Messenger()

    messenger.message(['running'])

    # filename_wav = utils.FILE_WAV  # args.filename

    # filename_clips_export = utils.FILE_CLIPS_EXPORT

    # # length of Ableton live track in beats
    #
    # beats_length_track_live = args.beats_length_track_live
    #
    # # beat start
    #
    # beat_start = args.beat_start
    #
    # # beat end
    #
    # beat_end = args.beat_end
    #
    # # length of wav file in s
    # y, sr = librosa.load(filename_wav)
    #
    # duration_s_audio = librosa.get_duration(y=y, sr=sr)
    #
    # s_beat_start = (beat_start / beats_length_track_live) * duration_s_audio
    #
    # s_beat_end = (beat_end / beats_length_track_live) * duration_s_audio
    #
    # data_chords = ir.extract_chords(
    #     filename_wav
    # )
    #
    # s_to_label_chords: List[Dict[float, Any]] = data_chords
    #
    # non_empty_chords = vamp_filter.vamp_filter_non_chords(
    #     s_to_label_chords
    # )
    #
    # events_chords: Dict[float, music21.chord.Chord] = vamp_convert.vamp_chord_to_dict(
    #     non_empty_chords
    # )
    #
    # df_chords = prep_vamp.chords_to_df(
    #     events_chords
    # )
    #
    # df_upper_voicings = postp_mxl.extract_upper_voices(
    #     df_chords
    # )
    #
    # chord_tree = song.MeshSong.get_interval_tree(
    #     df_upper_voicings
    # )
    #
    # mesh_song = song.MeshSong()
    #
    # data_beats = ir.extract_beats(
    #     filename_wav,
    #     from_cache=True
    # )
    #
    # beatmap = prep_vamp.extract_beatmap(
    #     data_beats
    # )
    #
    # mesh_song.set_tree(
    #     chord_tree,
    #     type='chord'
    # )
    #
    # mesh_song.quantize(
    #     beatmap,
    #     s_beat_start,
    #     s_beat_end,
    #     columns=['chord']
    # )
    #
    # # index beat, index ms audio file, index beat live audio track
    # df_with_live_audio_index = song.MeshSong.add_live_index(
    #     mesh_song.data_quantized,
    #     beat_start_live=beat_start,
    #     beat_end_live=beat_end,
    #     beats_length_track_live=beats_length_track_live
    # )
    #
    # # TODO: save Live JSON for chords synced with audio track in Live
    #
    # dict_write_json_live = song.MeshSong.to_json_live(
    #     df_with_live_audio_index,
    #     columns=['chord']
    # )
    #
    # utils.to_json_live(
    #     dict_write_json_live,
    #     filename_chords_to_live=filename_chords_to_live
    # )
    #
    # score_chords = postp_mxl.df_grans_to_score(
    #     df_with_live_audio_index,
    #     parts=['chord']
    # )
    #
    # postp_mxl.freeze_stream(
    #     stream=score_chords,
    #     filepath=utils.CHORD_SCORE
    # )

    # TODO: implement
    score_clips = postp_mxl.from_json(
        utils.FILE_CLIPS_EXPORT
    )

    score_clips.show()

    exit(0)

    # TODO: implement
    postp_mxl.freeze_stream(
        stream=score_clips,
        filepath=utils.CLIPS_EXPORT
    )

    messenger.message(['done'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process exported JSON of Ableton Live clips')

    # parser.add_argument('beats_length_track_live', help='length of track in Live')
    #
    # parser.add_argument('beat_start', help='first beat in Live')
    #
    # parser.add_argument('beat_end', help='last beat in Live')

    args = parser.parse_args()

    main(args)