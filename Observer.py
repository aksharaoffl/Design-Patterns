from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, notification: str):
        pass


class Subscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, notification: str):
        print(f"{self.name} received : {notification}")


class YoutubeChannel:
    def __init__(self, channel_name: str):
        self.channel_name = channel_name
        self.subscribers: list[Observer] = []

    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)
        print(f"{observer.name} got subscribed to {self.channel_name} ")

    def notify_subs(self, notification: str):
        for sub in self.subscribers:
            sub.update(notification)

    def upload_video(self, title: str):
        print(f"{self.channel_name} uploaded a new video : {title}")
        self.notify_subs(f"New Video: {title} posted")


if __name__ == "__main__":
    sub1 = Subscriber("Akshara")
    sub2 = Subscriber("Divu")

    yt_channel = YoutubeChannel("SheCodes :> ")

    yt_channel.subscribe(sub1)
    yt_channel.subscribe(sub2)
    yt_channel.upload_video("Day in the life of SDE at ABC")

