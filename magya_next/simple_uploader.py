"""
Magya Next - Simple Uploader for Personal Superintelligence
Codename: Nexus Extension
Author: AMMARICA1791 / Ammar
"""

from datetime import datetime

class MagyaNextNode:
    def __init__(self, title, link):
        self.id = f"magya-{datetime.now().strftime('%Y%m%d-%H%M')}"
        self.title = title
        self.link = link
        self.type = "AI_NEWS"
        self.status = "ready_for_youtube_and_instagram"
    
    def to_dict(self):
        return {
            "node_id": self.id,
            "type": self.type,
            "title": self.title,
            "source_url": self.link,
            "created_at": datetime.now().isoformat(),
            "platforms": ["youtube_magya_next", "instagram_magya_next"],
            "graph_relation": "belongs_to: MagyaNext Channel"
        }

if __name__ == "__main__":
    news = MagyaNextNode(
        title="Breaking AI News: New model released",
        link="https://news.google.com/rss/search?q=AI"
    )
    print("✅ Node created:", news.to_dict())
