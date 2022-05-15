import pyaudio, wave, threading, time, sys


class Player(threading.Thread):
    def __init__(self,file):
        self.wf = wave.open(file)
        self.p = pyaudio.PyAudio()


    def callback(self,in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def run(self):
        stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True,
                        stream_callback=self.callback)

        stream.start_stream()
        while stream.is_active():
            time.sleep(0.1)
        stream.stop_stream()
        stream.close()
        self.wf.close()
        self.p.terminate()

def main():
    file = sys.argv[1]
    Player(file).run()

if __name__ == '__main__':
    main()
    


