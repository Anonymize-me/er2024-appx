# Some global constants
ORIG_DIR = r'.\raw-data\\' # Dir. with original raw data
ORIG_IMO_DIR = ORIG_DIR + r'imo-data\\'  # iMotions' raw data dir.
ORIG_EMI_DIR = ORIG_DIR + r'emi-data\\'            # EyeMind's raw data dir.
DATA_DIR = r'out-data\\'                        # Output data dir.

# Dir. and file patterns
DIR_TXTPATTERN = r'S(P\d{2})-.+'            # Sub-dir for raw data
IMO_FILE_TXTPATTERN = r'\d{3}_(P\d{2}).csv' 
EMI_FILE_TXTPATTERN = r'EyeMind_EyeMind_(.+?)_collected-data.json'

# Participants
PARTICIPANTS = [f'P{x:02d}' for x in range(1,51)]
PARTICIPANT_SETS = {
    'set1': PARTICIPANTS.copy(), # all participants /!\ USED in data preproc pipeline
    'set2': ['P01', 'P11'], # No affectiva /!\ USED in data preproc pipeline
    'set3': ['P13', 'P15', 'P25', 'P34'] # Not auto synched with EMi /!\ USED in data preproc pipeline
}
[PARTICIPANT_SETS['set1'].remove(x) for x in PARTICIPANT_SETS['set2']]
[PARTICIPANT_SETS['set1'].remove(x) for x in PARTICIPANT_SETS['set3']]


IMO_COLS_DICT = {
    'Row': int, 'Timestamp': float, 
    'EventSource': int, 'SlideEvent': str, 'StimType': str, 'Duration': int, 'CollectionPhase': str, 'SourceStimuliName': str, 
    'EventSource': int, 'InputEventSource': str, 'Data': str, 'StimType': str,
    'EventSource': int,
    'ET_GazeLeftx': int, 'ET_GazeLefty': int, 'ET_GazeRightx': int, 'ET_GazeRighty': int, 
    'ET_PupilLeft': float, 'ET_PupilRight': float, 'ET_TimeSignal': float, 'ET_DistanceLeft': float, 'ET_DistanceRight': float, 
    'ET_CameraLeftX': float, 'ET_CameraLeftY': float, 'ET_CameraRightX': float, 'ET_CameraRightY': float,
    'ET_ValidityLeft': int, 'ET_ValidityRight': int,
    'EventSource': int, 'Event Group': int, 'Event Label': int, 'Event Text': int, 'Event Index': int,
    'EventSource': int, 'Gaze X': int, 'Gaze Y': int, 'Interpolated Gaze X': float, 'Interpolated Gaze Y': float, 'Interpolated Distance': float,
    'Gaze Velocity': float, 'Gaze Acceleration': float,
    'Fixation Index': int, 'Fixation Index by Stimulus': int, 'Fixation X': float, 'Fixation Y': float,
    'Fixation Start': float, 'Fixation End': float, 'Fixation Duration': float, 'Fixation Dispersion': float,
    'Saccade Index': int, 'Saccade Index by Stimulus': int,
    'Saccade Start': int, 'Saccade End': int, 'Saccade Duration': int,
    'Saccade Amplitude': float, 'Saccade Peak Velocity': float, 'Saccade Peak Acceleration': float, 'Saccade Peak Deceleration': float, 'Saccade Direction': float
}
IMO_COLS_DICT['SampleNumber'] = int
IMO_AFFECTIVA_FEATURES = ['Anger', 'Contempt', 'Disgust', 'Fear',
       'Joy', 'Sadness', 'Surprise', 'Engagement', 'Valence', 'Sentimentality',
       'Confusion', 'Neutral', 'Attention', 'Brow Furrow', 'Brow Raise',
       'Cheek Raise', 'Chin Raise', 'Dimpler', 'Eye Closure', 'Eye Widen',
       'Inner Brow Raise', 'Jaw Drop', 'Lip Corner Depressor', 'Lip Press',
       'Lip Pucker', 'Lip Stretch', 'Lip Suck', 'Lid Tighten', 'Mouth Open',
       'Nose Wrinkle', 'Smile', 'Smirk', 'Upper Lip Raise', 'Blink',
       'BlinkRate', 'Pitch', 'Yaw', 'Roll']
for affect in IMO_AFFECTIVA_FEATURES: IMO_COLS_DICT[affect] = float

diffMappingToScore = {'Very easy':0, 'Easy':1, 'Neutral':2, 'Difficult':3, 'Very difficult':4}

QUESTIONS_TYPES = {
    'Type1': ['Coarse', 'Fine'],
    'Type2': ['MainQuestion', 'DifficultyQuestion'],
    'Type3': ['essentialComlexity','accidentalComlexity'],
    'Type4': ['Simple', 'DiffSimple', 'Complex', 'DiffComplex']
}

EMI_CAMUNDA_OBJ_ID_PATTERNS = [
    'Activity_', 'Flow_', 'Gateway_', 
    'title_', 'question_area_', 'answer_area_', 'option_answer_', 
    'next_button_'
    'ukn'
]
EMI_SELECTED_OBJ_ID_PATTERNS = ['Activity_', 'Flow_', 'Gateway_', 'question_area_', 'next_button_']
EMI_ACTIVITY_OBJ_ID_PATTERNS = ['Activity_', 'Flow_', 'Gateway_']