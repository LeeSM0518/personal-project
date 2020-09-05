package dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class PutOneSeatByDeviceDto {

  private int studentId;
  private int roomId;
  private int seatNumber;

}
