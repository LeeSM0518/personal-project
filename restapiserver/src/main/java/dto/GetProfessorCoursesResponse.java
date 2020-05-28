package dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.sql.Time;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class GetProfessorCoursesResponse {

  private int id;
  private String title;
  private Time startTime;
  private Time endTime;
  private int _class;
  private String day;
  private String dong;
  private String ho;

  public GetProfessorCoursesResponse(Course course) {
    id = course.getId();
    title = course.getTitle();
    startTime = course.getStartTime();
    endTime = course.getEndTime();
    _class = course.get_class();
    day = course.getDay();
    dong = course.getDong();
    ho = course.getHo();
  }

}
