"""Holds an abstract class defining a flags source."""
from os import path

from ..tools import SearchScope


class FlagsSource(object):
    """An abstract class defining a Flags Source."""

    def __init__(self, include_prefixes):
        """Initialize default flags storage."""
        self._include_prefixes = include_prefixes

    def get_flags(self, file_path=None, search_scope=None):
        """Get flags for a view path [ABSTRACT].

        Raises:
            NotImplementedError: Should not be called directly.
        """
        raise NotImplementedError("calling abstract method")

    @staticmethod
    def _update_search_scope(search_scope, file_path):
        if search_scope:
            # we already know what we are doing. Leave search scope unchanged.
            return search_scope
        # search database from current file up the tree
        return SearchScope(from_folder=path.dirname(file_path))

    def _get_cached_from(self, file_path):
        """Get cached path for file path.

        Args:
            file_path (str): Input file path.

        Returns:
            str: Path to the cached flag source path.
        """
        if file_path and file_path in self._cache:
            return self._cache[file_path]
        return None
