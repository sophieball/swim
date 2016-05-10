#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "dynarray.h"
#include "hashmap.h"

#define KEY_MAX_LENGTH (256)

typedef struct data_struct_s
{
    char *key_string;
    int number;
} data_struct_t;

/*void printArr(DynArray_T dyn){
  FILE *out = fopen("arrout", "w");
  int len = DynArray_getLength(dyn);
  int i;
  char *str;
  for(i = 1; i < len; i++){
    str = (char*)DynArray_get(dyn, i);
    fprintf(out, "%s\n", str);
  }
  fclose(out);
}*/

int main(int argc, char **argv){
  FILE *in = fopen(argv[1], "r");
  FILE *out = fopen(argv[2], "w");
  FILE *arr = fopen("arrout", "w");
  char *line = NULL;
  size_t length = 0;
  map_t hashmapTime, hashmapIp;
  char key_string[KEY_MAX_LENGTH];
  data_struct_t* value, *fromHash;
  int dynarrayIndex = 1, dynarrayIndexIp = 1;
  int iStart, iEnd, iIp;
  DynArray_T dynarrayTime, dynarrayIp;
  char *substr, *subdest;
  int numToWrite;
  char *dot;
  int error;//return value from hashmap functions

  hashmapTime = hashmap_new();//used to store the key - value pair so that we know where in the array we should put the time
  dynarrayTime = DynArray_new(1000);//used to store the value - key pair
  hashmapIp = hashmap_new();//used to store the key - value pair so that we know where in the array we should put the IP
  dynarrayIp = DynArray_new(1000);//used to store the value - key pair

  getline(&line, &length, in);
  while(line){
    getline(&line, &length, in);
    getline(&line, &length, in);

    value = (data_struct_t*)malloc(sizeof(data_struct_t));
    substr = strtok(line, ",");
    value->key_string = (char*)malloc(strlen(substr)+1);
    strncpy(value->key_string, substr, strlen(substr));
    value->key_string[strlen(substr)] = '\0';
    error = hashmap_get(hashmapTime, value->key_string, (void**)&fromHash);
    if(error == MAP_MISSING){
      iStart = dynarrayIndex;
      //insert
      dot = strstr(substr, ".\0");
      *dot = '\0';
      value->number = iStart;
      error = hashmap_put(hashmapTime, substr, value);
      if(error != MAP_OK) continue;
      //put it into dynarray
      DynArray_add(dynarrayTime, value->key_string);
      dynarrayIndex ++;
    }
    else if(error == MAP_OK){
      iStart = fromHash->number;
    }


    value = (data_struct_t*)malloc(sizeof(data_struct_t));
    substr = strtok(NULL, ",");
    value->key_string = (char*)malloc(strlen(substr)+1);
    strncpy(value->key_string, substr, strlen(substr));
    value->key_string[strlen(substr)] = '\0';
    error = hashmap_get(hashmapTime, value->key_string, (void**)&fromHash);
    if(error == MAP_MISSING){
      iEnd = dynarrayIndex;
      //insert
      dot = strstr(substr, ".\0");
      *dot = '\0';
      value->number = iEnd;
      error = hashmap_put(hashmapTime, substr, value);
      if(error != MAP_OK) continue;
      //put it into dynarray
      DynArray_add(dynarrayTime, value->key_string);
      dynarrayIndex ++;
    }
    else if(error == MAP_OK){
      iEnd = fromHash->number;
    }


    if(dynarrayIndexIp >= 42000){
      free(line);
      free(value);
      hashmap_free(hashmapTime);
      hashmap_free(hashmapIp);
      DynArray_free(dynarrayIp);
      DynArray_free(dynarrayTime);
      fclose(in);
      fclose(out);
      fclose(arr);
      return 0;
    }
    substr = strtok(NULL, ",");
    value = (data_struct_t*)malloc(sizeof(data_struct_t));
    subdest = strtok(NULL, ",");
    value->key_string = (char*)malloc(strlen(substr) + strlen(subdest) + 2);
    snprintf(value->key_string, strlen(substr) + strlen(subdest) + 1, "%s %s", substr, subdest);
    //strncpy(value->key_string, strcat(substr, subdest), strlen(substr) + strlen(subdest));
    //value->key_string[strlen(substr) + strlen(subdest)] = '\0';
    error = hashmap_get(hashmapIp, value->key_string, (void**)&fromHash);
    if(error == MAP_MISSING){
      iIp = dynarrayIndexIp;
      printf("ip index %s\n", value->key_string);
      //insert
      value->number = iIp;
      error = hashmap_put(hashmapIp, value->key_string, value);
      if(error != MAP_OK) continue;
      //put it into dynarray
      DynArray_add(dynarrayIp, value->key_string);
      fprintf(arr, "%d %s\n", dynarrayIndexIp, value->key_string);
      dynarrayIndexIp ++;
    }
    else if(error == MAP_OK){
      iIp = fromHash->number;
    }
/*
    value = (data_struct_t*)malloc(sizeof(data_struct_t));
    substr = strtok(NULL, ",");
    value->key_string = (char*)malloc(strlen(substr)+1);
    strncpy(value->key_string, substr, strlen(substr));
    value->key_string[strlen(substr)] = '\0';
    error = hashmap_get(hashmapIp, value->key_string, (void**)&fromHash);
    if(error == MAP_MISSING){
      iIp = iIp * 100000 + dynarrayIndexIp;
      printf("ip index %d\n", dynarrayIndexIp);
      //insert
      value->number = dynarrayIndexIp;
      error = hashmap_put(hashmapIp, substr, value);
      if(error == MAP_OMEM) fprintf(stderr, "mem %d\n", dynarrayIndexIp);
      //put it into dynarray
      DynArray_add(dynarrayIp, value->key_string);
      dynarrayIndexIp ++;
    }
    else if(error == MAP_OK){
      iIp = iIp * 100000 + fromHash->number;
      fprintf(stderr, "found\n");
    }*/
    fprintf(out, "%u %u 1 %u\n", iStart, iEnd, iIp);//write line

  }

  free(line);
  free(value);
  DynArray_free(dynarrayIp);
  DynArray_free(dynarrayTime);
  fclose(in);
  fclose(out);

  return 0;
}
