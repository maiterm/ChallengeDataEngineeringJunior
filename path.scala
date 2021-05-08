import scala.collection.mutable.ListBuffer
object path{
def generateMonthlyPathList(year: String, month:String, day:String): List[String] = {
    //Implementación de tu solución
    var paths = new ListBuffer[String]()
    val path = "https://importantdata@location/"
    var pathday = ""
    for (d <- 1 to day.toInt){
      pathday = s"${path}${year}/${month}/${if (d < 10) "0"+d else d  }/"
      paths +=  pathday
    }
    paths.toList}
def main (args:Array[String]):Unit ={
  val paths = generateMonthlyPathList("2021", "05", "17")
  paths.foreach(path => println(path))
  }
}