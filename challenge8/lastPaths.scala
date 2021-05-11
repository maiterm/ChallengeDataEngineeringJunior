import java.time.format.DateTimeFormatter
import java.time.LocalDate
import scala.collection.JavaConverters._
object lastPaths{
def generateLastDaysPaths(date: String, days:Int): List[String] = {
    def dateInputFormat = DateTimeFormatter.ofPattern("yyyyMMdd")
    def dateOutputFormat = DateTimeFormatter.ofPattern("yyyy/MM/dd")
    val path = "https://importantdata@location/"
    val endDateWithFormat = LocalDate.parse(date, dateInputFormat).plusDays(1)
    val startDate = endDateWithFormat.minusDays(days)
    val dates = startDate.datesUntil(endDateWithFormat).iterator().asScala.map(date => s"${path}${dateOutputFormat.format(date)}/").toList
    dates    
    }
def main (args:Array[String]):Unit ={
  val paths = generateLastDaysPaths("20210410", 10)
  paths.foreach(path => println(path))
  }
}