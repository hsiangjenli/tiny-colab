package com.hsiangjenli;

import com.enofex.taikai.Taikai.Builder;
import org.junit.jupiter.api.Test;

public class ArchitectureTest {

  @Test
  void shouldValidateJavaRules() {
    Builder builder = new Builder();
    builder.namespace("com.hsiangjenli").java(ArchitectureRules.BASE_JAVA_RULES).build().checkAll();
  }
}
