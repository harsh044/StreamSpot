from fastapi import status


# code : [message, response http code]
messages = {
    1000: ["User Authenticated Not Successfully.", status.HTTP_401_UNAUTHORIZED,False],
    1001: ["User Authenticated Successfully.", status.HTTP_200_OK,True],
    1002: ["Data Featch Successfully.", status.HTTP_200_OK,True],
    1004: ["Data Add Successfully.", status.HTTP_200_OK,True],
    1005: ["Something Went Wrong.", status.HTTP_400_BAD_REQUEST,False],
    1006: ["Data Updated Successfully.", status.HTTP_200_OK,True],
    1008: ["No Data found.", status.HTTP_404_NOT_FOUND,False],
    1009: ["File Already Exists.", status.HTTP_400_BAD_REQUEST,False],
    1010: ["Data Sync Successfully.", status.HTTP_200_OK,True],
    1011: ["Data Sync Failed.", status.HTTP_400_BAD_REQUEST,False],
    1012: ["Data Already Exist.", status.HTTP_200_OK,True],
}
