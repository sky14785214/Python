
fun main(args: Array<String>){
    //var plaintext = "說是寂寞的秋的清愁，說是遙遠的海的相思。假如有人問我的憂愁，我不敢說出你的名子。我不敢說出你的名子，假如有人問我的憂愁:說是遙遠的海的相思，說是寂寞的秋的清愁。"
    var plaintext = "do not judge a book by its cover. Do not judge me from my outside."
    println("plaintext: $plaintext")
    //var text_mode = "Chinese"
    var text_mode = "English"
    val key_type = 256
    var key_str = "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
    var plaintext_len = if(plaintext.length != null) plaintext.length else -1

    // 字串轉16進字
    fun stringToHexString(string: String): String {
        var c = CharArray(string.length)
        c = string.toCharArray()
        var hesStr = ""
        for (i in c.indices) {
            hesStr = hesStr + Integer.toHexString(c[i].toInt())
        }
        return hesStr
    }

//    fun hexStringToString(String string){
//        var String sub = "";
//        for (int i = 0; i < string.length() / 2; i++) {
//        var sub = sub + (char) Integer.valueOf(string.substring(i * 2, i * 2 + 2),16).byteValue();
//
//    }
//        return sub;
//    }

    var plaintext_hex:String = stringToHexString(plaintext)
    println(plaintext_hex)
    val dd = 128/4
    var phex_leng = plaintext_hex.length
    println(phex_leng)
    var q:Int = phex_leng/dd
    var r:Int = phex_leng%dd
//    println(q)
//    println(r)
    if (r != 0){
        q = q+1
        plaintext_hex = plaintext_hex+"8"
        for ( i in 1..dd-r-1){
            plaintext_hex = plaintext_hex+ "0"
        }
    }
    // println(plaintext_hex)

    // encryption
    var ciphertext:String
    
//    for( i in q){
//
//    }






    if (text_mode.equals("Chinese")){  // equals 判斷相同
        //print(plaintext_len)
        //println("中文")
//        for(i in plaintext_len){
//        }

    }
    else if(text_mode == ("English")){
        //println(plaintext_len)
        //println("英文")
    }

}
// 字串轉utf8
//fun StrtoUtf(a: String)  : Unit{
//    var charset = Charsets.UTF_8
//    var test = a
//    var testhex = test.toByteArray(charset)
//    println(testhex.contentToString()) // [72, 101, 108, 108, 111]
//    //println(testhex.toString(charset)) // Hello
//}



