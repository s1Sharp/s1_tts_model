import os
import torch

from typing import List

latest_model_url = 'https://models.silero.ai/models/tts/ru/v4_ru.pt'

class Speakers:
    available_speakers = ['aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random']

    @staticmethod
    def speaker_awail(speaker: str):
        return speaker in Speakers.available_speakers

    @staticmethod
    def check_speakers(speaker_list):
        return all(
                map(lambda x: Speakers.speaker_avail(x), speaker_list)
            )


class TtsModel:
    def __init__(self,
                local_model_filename: str,
                speakers: List[str],
                sample_rate: int,
                model_url: str = latest_model_url,
                num_threads: int = 4,
                torch_device_type: str = 'cpu') -> None:
        torch.set_num_threads(num_threads)
        self.device = torch.device(torch_device_type)
        self.sample_rate = sample_rate

        if not os.path.isfile(local_model_filename):
            torch.hub.download_url_to_file(
                model_url,
                local_model_filename)  

        self.model = torch.package \
                        .PackageImporter(local_model_filename) \
                        .load_pickle("tts_models", "model") \
                        .to(self.device)
        if len(speakers) == 0 or not Speakers.check_speakers(speaker_list=speakers):
            speakers = Speakers.available_speakers
        self.speakers = speakers
    
    def tts_text_to_audio(self, text: str, speaker: str, sample_rate: int = None, use_ssml: bool = False):
        if sample_rate is None:
            sample_rate = self.sample_rate
        if not Speakers.speaker_awail(speaker) or speaker not in self.model.speakers:
            raise RuntimeError(f"Speaker {speaker} not available")
        if use_ssml:
            return self.model.apply_tts(
                    ssml_text=text,
                    speaker=speaker,
                    sample_rate=sample_rate,
                )
        else:
            return self.model.apply_tts(
                    text=text,
                    speaker=speaker,
                    sample_rate=sample_rate,
                )

    def tts_text_to_audio_local(self, text: str, speaker: str, file_path:str, sample_rate: int = None):
        if sample_rate is None:
            sample_rate = self.sample_rate
        if not Speakers.speaker_awail(speaker) or speaker not in self.model.speakers:
            raise RuntimeError(f"Speaker {speaker} not available")

        return self.model.save_wav(
                text=text,
                speaker=speaker,
                sample_rate=sample_rate,
                audio_path=file_path,
            )
