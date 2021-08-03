import pickle
import numpy as np

class SplitTimePredictor:

    file_path_5 = '../models/main_model_5.pkl'
    file_path_10 = '../models/main_model_10.pkl'
    file_path_15 = '../models/main_model_15.pkl'
    file_path_20 = '../models/main_model_20.pkl'
    file_path_25 = '../models/main_model_25.pkl'
    file_path_30 = '../models/main_model_30.pkl'
    file_path_35 = '../models/main_model_35.pkl'
    file_path_40 = '../models/main_model_40.pkl'
    
    def __init__(self):
        # Load 5km model
        with open(self.file_path_5, 'rb') as f:
            self.model_5 = pickle.load(f)
        
        # Load 10km model
        with open(self.file_path_10, 'rb') as f:
            self.model_10 = pickle.load(f)
        
        # Load 15km model
        with open(self.file_path_15, 'rb') as f:
            self.model_15 = pickle.load(f)
        
        # Load 20km model
        with open(self.file_path_20, 'rb') as f:
            self.model_20 = pickle.load(f)
        
        # Load 25km model
        with open(self.file_path_25, 'rb') as f:
            self.model_25 = pickle.load(f)
        
        # Load 30km model
        with open(self.file_path_30, 'rb') as f:
            self.model_30 = pickle.load(f)
        
        # Load 35km model
        with open(self.file_path_35, 'rb') as f:
            self.model_35 = pickle.load(f)
        
        # Load 40km model
        with open(self.file_path_40, 'rb') as f:
            self.model_40 = pickle.load(f)
    
    
    def time_to_seconds(self, time):
        if ':' in time:
            time_parts = time.split(':')
            seconds = int(time_parts[-1]) + (int(time_parts[-2]) * 60)
            if len(time_parts) > 2:
                seconds += int(time_parts[-3]) * 3600
            return int(seconds)
        else:
            return np.nan
    
    
    def seconds_to_time(self, time):
        hours = time // 3600
        time -= hours*3600
        hours = str(int(hours))
        if len(hours) < 2:
            hours = '0' + hours
        
        minutes = time // 60
        time -= minutes*60
        minutes = str(int(minutes))
        if len(minutes) < 2:
            minutes = '0' + minutes
            
        seconds = str(int(time))
        if len(seconds) < 2:
            seconds = '0' + seconds
        
        if hours != '00':
            return hours + ':' + minutes + ':' + seconds
        return minutes + ':' + seconds
    
    
    def predict_finishing_time(self, splits):
        # Convert splits to seconds
        splits = [self.time_to_seconds(x) for x in splits]
        
        # Predict time (seconds) left to run
        remaining_time = 0
        if len(splits) == 1:
            remaining_time = self.model_5.predict([splits])[0]
        elif len(splits) == 2:
            remaining_time = self.model_10.predict([splits])[0]
        elif len(splits) == 3:
            remaining_time = self.model_15.predict([splits])[0]
        elif len(splits) == 4:
            remaining_time = self.model_20.predict([splits])[0]
        elif len(splits) == 5:
            remaining_time = self.model_25.predict([splits])[0]
        elif len(splits) == 6:
            remaining_time = self.model_30.predict([splits])[0]
        elif len(splits) == 7:
            remaining_time = self.model_35.predict([splits])[0]
        elif len(splits) == 8:
            remaining_time = self.model_40.predict([splits])[0]
        else:
            raise ValueError('Wrong number of splits passed.')
        
        # Calculate total time
        total_time = sum(splits) + remaining_time
        
        return self.seconds_to_time(total_time)