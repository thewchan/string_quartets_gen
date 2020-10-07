\version "2.20" 
\include "lilypond-book-preamble.ly"
    
color = #(define-music-function (parser location color) (string?) #{
        \once \override NoteHead #'color = #(x11-color color)
        \once \override Stem #'color = #(x11-color color)
        \once \override Rest #'color = #(x11-color color)
        \once \override Beam #'color = #(x11-color color)
     #})
    
\header { } 
\score  { 
 
      << \new Staff  = xawzcdyeefxxcca { \time 4/4
             r 4  
             a' 8  
             r 8  
             g' 8  
             r 8  
             c'' 8  
             r 8  
             b' 4.  
             r 4.  
             a' 8  
             r 8  
             g' 8  
             r 8  
             d'' 8  
             r 8  
             c'' 4.  
             r 4.  
             g'' 8  
             r 8  
             e'' 8  
             r 8  
             c'' 8  
             r 8  
             b' 8  
             r 8  
             a' 4.  
             r 4.  
             e'' 8  
             r 8  
             c'' 8  
             r 8  
             d'' 8  
             r 8  
             c'' 4.  
              } 
            
 
       \new Staff  = xawzcdyeeezecwe { \time 4/4
             fis' 4.  
             e' 2  
             d' 4  
             e' 4  
             f' 4  
             g' 4  
             f' 4  
             g' 4  
             e' 4  
             f' 4  
             g' 1  ~  
             g' 4  
             a' 4  
             gis' 4  
             a' 1.  
              } 
            
 
       \new Staff  = xawzcdyeefzfcxc { \time 4/4
             d' 8  
             c' 4  
             b 4  
             a 4  
             b 4  
             g 4  
             d' 4  
             c' 2  
             b 2  
             a 4  
             g 4  
             a 4  
             b 4  
             c' 4  
             d' 4  
             e' 4  
             d' 4  
             c' 4  
             b 4  
             c' 4  
             d' 4  
             e' 2  
              } 
            
 
       \new Staff  = xawzcdyefybwwfc { \time 4/4
             d 8  
             ees 4  
             e 4  
             fis 4  
             g 4  
             c 4  
             d 4  
             g 2  
             g, 4  
             c 4  
             f 4  
             e 4  
             d 4  
             g 4  
             a 4  
             b 4  
             c' 4  
             b 4  
             a 2  
             a, 2  
             a 2  
              } 
            
 
        >>
      
  } 
 
\paper { }
\layout {
  \context {
    \RemoveEmptyStaffContext
    \override VerticalAxisGroup #'remove-first = ##t
  }
 }
 
