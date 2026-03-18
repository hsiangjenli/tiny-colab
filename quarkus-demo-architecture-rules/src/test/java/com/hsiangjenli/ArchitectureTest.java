package com.hsiangjenli;

import com.enofex.taikai.Taikai;
import org.junit.jupiter.api.Test;

public class ArchitectureTest {

  @Test
  void shouldValidateJavaRules() {
    Taikai.builder().namespace("com.hsiangjenli").java(ArchitectureRules.BASE_JAVA_RULES).build().checkAll();
  }
}
