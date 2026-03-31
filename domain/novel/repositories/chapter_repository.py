from abc import ABC, abstractmethod
from typing import List, Optional
from domain.novel.entities.chapter import Chapter
from domain.novel.value_objects.novel_id import NovelId


class ChapterRepository(ABC):
    """章节仓储接口"""

    @abstractmethod
    def save(self, chapter: Chapter) -> None:
        """保存章节"""
        pass

    @abstractmethod
    def get_by_id(self, chapter_id: str) -> Optional[Chapter]:
        """根据 ID 获取章节"""
        pass

    @abstractmethod
    def list_by_novel(self, novel_id: NovelId) -> List[Chapter]:
        """列出小说的所有章节"""
        pass

    @abstractmethod
    def delete(self, chapter_id: str) -> None:
        """删除章节"""
        pass
