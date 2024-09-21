
  streamlit. elements. empty. EmptyMixin
@gather_metrics("empty") def empty(self) -> DeltaGenerator
 
Insert a single-element container.  Inserts a container into your app that can be used to hold a single element. This allows you to, for example, remove elements at any point, or replace several elements at once (using a child multi-element container).  To insert/ replace/ clear an element on the returned container, you can use ``with`` notation or just call methods directly on the returned object. See examples below.  Examples -------- Overwriting elements in-place using ``with`` notation: 
