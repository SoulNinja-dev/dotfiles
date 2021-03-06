"""
Sane headers.

Allow for a header implementation that requires `#` headers to have a space
after the `#` portion. This allows for things like Magiclink issues to work
at the beginning of lines, and potentially other things like tag extensions
etc.
"""
import re
from ..markdown import Extension
from ..markdown.blockprocessors import HashHeaderProcessor


class SaneHeadersProcessor(HashHeaderProcessor):
    """Process hash headers syntax."""

    RE = re.compile(r'(?:^|\n)(?P<level>#{1,6})(?=[ ])(?P<header>(?:\\.|[^\\])*?)#*(?:\n|$)')


class SaneHeadersExtension(Extension):
    """Adds the sane headers extension."""

    def extendMarkdown(self, md):
        """Extend the inline and block processor objects."""

        md.parser.blockprocessors.register(SaneHeadersProcessor(md.parser), 'hashheader', 70)
        md.registerExtension(self)


def makeExtension(*args, **kwargs):
    """Return extension."""

    return SaneHeadersExtension(*args, **kwargs)
