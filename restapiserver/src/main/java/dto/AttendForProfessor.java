package dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class AttendForProfessor {

  private int id;
  private int studentCode;
  private String name;
  private int count;
  private double sum;

}
