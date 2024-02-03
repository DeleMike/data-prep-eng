from helpers import remove_accents_and_underdots

def remove():
    # Bí a bá lo òṣùwọ̀n ìṣẹ̀dá, gbogbo gbólóhùn èdè Yorùbá ni a lè pín sí méjì ní gbòòrò báyìí
    # text = "Ǹjẹ́ ọmọ náà ní owó?"
    text = 'Bí ọ̀rọ̀-arọ́pò-orúkọ gígùn bá jẹ́orí nínú àpólà-orúkọ tí o lò gẹ́gẹ́bí ẹ̀yán ajórúkọ, o ní àǹfàní láti fi ọ̀rọ̀-arọ́pò-orúkọ kúkúrú tó bá ọ̀rọ̀-arọ́pò-orúkọ gígùn bẹ́ẹ̀ mu ní iye àti ẹni rọ́pò ní ipò tí o ti gbé ẹ̀yán ajórúkọ bẹ́ẹ̀'
    return remove_accents_and_underdots(text).strip('\n')

print(remove())
