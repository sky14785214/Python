
fun main(args: Array<String>){
    //var plaintext = "說是寂寞的秋的清愁，說是遙遠的海的相思。假如有人問我的憂愁，我不敢說出你的名子。我不敢說出你的名子，假如有人問我的憂愁:說是遙遠的海的相思，說是寂寞的秋的清愁。"
    var plaintext = "do not judge a book by its cover. Do not judge me from my outside."
    println("plaintext: $plaintext")
    //var text_mode = "Chinese"
    var text_mode = "English"
    val key_type = 256
    var key_str = "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
    var plaintext_len = if(plaintext.length != null) plaintext.length else -1
    var a = "b"


    fun Strunicode(str: String): String {
        return String(str.toByteArray())
    }
    val b = Strunicode(a)
    println(b)


    if (text_mode.equals("Chinese")){  // equals 判斷相同
        print(plaintext_len)
        println("中文")

    }
    else if(text_mode == ("English")){
        println(plaintext_len)
        println("英文")
    }
}


//
//fun utf8ToUnicodeNoPrefix(str: String) : String {
//    val builder = StringBuilder()
//    for (c in str.iterator()) {
//        val item = Integer.toHexString(c.toInt())
//        builder.append(upToNString(item, 4))
//    }
//    return builder.toString()
//}

