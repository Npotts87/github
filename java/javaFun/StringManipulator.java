public class StringManipulator {
    public String trimAndConcat(String str1, String str2) {
        str1 = str1.trim();
        str2 = str2.trim();
        return str1 + str2;
    }
    public Integer getIndexOrNull(String str1, String str2) {
        int index =str1.indexOf(str2);
        if (index < 0){
            return null;
        }
        return index;
    }
    public Integer getIndexOrNull(String string, char character) {
        int index =string.indexOf(character);
        if (index < 0){
            return null;
        }
        return index;
    }
    public String concatSubstring(String str1, int int1, int int2, String str2) {
        str1 = str1.substring(int1, int2);
        return str1 + str2;
    }
}